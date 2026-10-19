"""Check cow-py order hashing/UID and ECDSA owner recovery against live auction bodies
from the public solver-instances bucket (one latest auction per chain)."""
import json, urllib.request, gzip, io, sys, collections
from eth_account import Account
from eth_utils import keccak, to_hex
from web3 import Web3
from cowdao_cowpy.contracts.domain import TypedDataDomain
from cowdao_cowpy.contracts.order import Order, hash_order, compute_order_uid

B="https://solver-instances.s3.eu-central-1.amazonaws.com"
CHAIN_ID={"mainnet":1,"xdai":100,"arbitrum-one":42161,"base":8453,"bnb":56,"polygon":137,"avalanche":43114,"linea":59144,"ink":57073,"plasma":9745}
SETTLEMENT="0x9008D19f58AAbD9eD0D60971565AA8510560ab41"
PREFIX=b"\x19Ethereum Signed Message:\n32"
ids=json.load(open("auctions/ids.json"))
def fetch(c,i):
    r=urllib.request.urlopen(urllib.request.Request(f"{B}/prod/{c}/auction/{i}.json",headers={"User-Agent":"Mozilla/5.0","Accept-Encoding":"gzip"}),timeout=60)
    b=r.read()
    if b[:2]==b"\x1f\x8b": b=gzip.decompress(b)
    return json.loads(b)
summary=[]; mismatches=[]
for c,cid in CHAIN_ID.items():
    if c not in ids or not ids[c]: continue
    a=fetch(c,ids[c][-1]); orders=a.get("orders",[])
    if orders and c=="mainnet": print("sample order keys:", sorted(orders[0].keys()))
    dom=TypedDataDomain("Gnosis Protocol","v2",cid,SETTLEMENT)
    cnt=collections.Counter(); ok=collections.Counter()
    for o in orders:
        scheme=o.get("signingScheme"); cnt[scheme]+=1
        receiver=o.get("receiver") or ""
        if receiver and int(receiver,16)==0: receiver=""
        try:
            order=Order(sell_token=Web3.to_checksum_address(o["sellToken"]),buy_token=Web3.to_checksum_address(o["buyToken"]),
                receiver=Web3.to_checksum_address(receiver) if receiver else "",sell_amount=str(o.get("fullSellAmount",o["sellAmount"])),buy_amount=str(o.get("fullBuyAmount",o["buyAmount"])),
                valid_to=o["validTo"],app_data=o["appData"],fee_amount=str(o.get("feeAmount","0")),kind=o["kind"],
                partially_fillable=o["partiallyFillable"],sell_token_balance=o.get("sellTokenSource",o.get("sellTokenBalance","erc20")),buy_token_balance=o.get("buyTokenDestination",o.get("buyTokenBalance","erc20")))
            uid=compute_order_uid(dom,order,Web3.to_checksum_address(o["owner"])).lower()
            uid_ok = uid==o["uid"].lower()
            digest=bytes(hash_order(dom,order))
            rec_ok=None
            if scheme in("eip712","ethsign"):
                d = keccak(PREFIX+digest) if scheme=="ethsign" else digest
                rec=Account._recover_hash(d,signature=o["signature"]).lower()
                rec_ok = rec==o["owner"].lower()
            if uid_ok and rec_ok in (True,None): ok[scheme]+=1
            else: mismatches.append((c,o["uid"],scheme,uid_ok,rec_ok,o.get("class"),o.get("partiallyFillable"),o.get("receiver")))
        except Exception as e:
            mismatches.append((c,o.get("uid"),scheme,"EXC",str(e)[:120]))
    summary.append((c,a.get("id"),len(orders),dict(cnt),dict(ok)))
for s in summary: print(f"{s[0]:13} auction {s[1]} orders={s[2]:4} schemes={s[3]} ok={s[4]}")
print("mismatches:",len(mismatches))
for m in mismatches[:40]: print(" ",m)
