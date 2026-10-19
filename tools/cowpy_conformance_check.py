"""Run cow-py against the cow-rs/services conformance fixture (chain 1, Anvil signer #0)."""
import json, sys
from eth_account import Account
from eth_account.messages import encode_typed_data, _hash_eip191_message, encode_defunct
from eth_utils import keccak, to_hex
from web3 import Web3
from cowdao_cowpy.contracts.domain import TypedDataDomain
from cowdao_cowpy.contracts.order import Order, hash_order, compute_order_uid, normalize_order, ORDER_TYPE_FIELDS
from cowdao_cowpy.contracts.sign import sign_order, SigningScheme

FIX = sys.argv[1]
d = json.load(open(FIX))
KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"  # Anvil account 0
acct = Account.from_key(KEY)
assert acct.address.lower() == d["signer"], (acct.address, d["signer"])
dom = TypedDataDomain(name="Gnosis Protocol", version="v2", chainId=d["chain_id"], verifyingContract=Web3.to_checksum_address(d["settlement"]))

def sig_hex(sig):  # fixture r,s,v -> 65-byte hex
    return "0x" + sig["r"][2:] + sig["s"][2:] + f"{sig['v']:02x}"

rows = []
for v in d["vectors"]:
    res = {"id": v["id"]}
    receiver = "" if (v["receiver"] is None or int(v["receiver"], 16) == 0) else Web3.to_checksum_address(v["receiver"])
    order = Order(sell_token=Web3.to_checksum_address(v["sell_token"]), buy_token=Web3.to_checksum_address(v["buy_token"]),
                  receiver=receiver, sell_amount=v["sell_amount"], buy_amount=v["buy_amount"], valid_to=v["valid_to"],
                  app_data=v["app_data"], fee_amount=v["fee_amount"], kind=v["kind"], partially_fillable=v["partially_fillable"],
                  sell_token_balance=v["sell_token_balance"], buy_token_balance=v["buy_token_balance"])
    try:
        norm = normalize_order(order)
        sm = encode_typed_data(domain_data=dom.to_dict(), message_types={"Order": ORDER_TYPE_FIELDS}, message_data=norm)
        res["domain_separator"] = to_hex(sm.header) == v["domain_separator"]
        res["hash_struct"] = to_hex(sm.body) == v["hash_struct"]
        digest = hash_order(dom, order)
        res["eip712_digest"] = to_hex(digest) == v["eip712_digest"]
        uid = compute_order_uid(dom, order, acct.address)
        res["uid"] = uid.lower() == v["uid"]
        s712 = sign_order(dom, order, acct, SigningScheme.EIP712).data
        res["eip712_signature"] = s712.lower() == sig_hex(v["eip712_signature"]).lower()
        res["eip712_recovered"] = Account._recover_hash(digest, signature=s712).lower() == v["eip712_recovered_owner"]
        # ethsign: what cow-py produces when asked for the ETHSIGN scheme
        seth = sign_order(dom, order, acct, SigningScheme.ETHSIGN).data
        res["ethsign_signature"] = seth.lower() == sig_hex(v["ethsign_signature"]).lower()
        expected_eth_digest = keccak(b"\x19Ethereum Signed Message:\n32" + bytes(digest))
        res["ethsign_digest_known"] = to_hex(expected_eth_digest) == v["ethsign_digest"]
        rec = Account._recover_hash(expected_eth_digest, signature=seth).lower()
        res["ethsign_recovered_via_cowpy_sig"] = rec
    except Exception as e:
        res["error"] = f"{type(e).__name__}: {e}"
    rows.append(res)

keys = ["domain_separator","hash_struct","eip712_digest","uid","eip712_signature","eip712_recovered","ethsign_signature","ethsign_digest_known"]
print(f"{'vector':34}" + "".join(f"{k[:14]:>15}" for k in keys))
for r in rows:
    if "error" in r:
        print(f"{r['id']:34} ERROR {r['error']}")
    else:
        print(f"{r['id']:34}" + "".join(f"{str(r[k]):>15}" for k in keys) + f"   ethsign-recovers-to={r['ethsign_recovered_via_cowpy_sig'][:12]}")
