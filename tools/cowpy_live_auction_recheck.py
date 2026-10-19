"""Re-verify every auction-DTO mismatch against the orderbook's canonical order record."""
import json, urllib.request, gzip, time, collections, sys
from eth_account import Account
from eth_utils import keccak
from web3 import Web3
from cowdao_cowpy.contracts.domain import TypedDataDomain
from cowdao_cowpy.contracts.order import Order, hash_order, compute_order_uid
exec(open("live_check.py").read().split("summary=[]")[0])  # reuse constants/fetch
API={"mainnet":"mainnet","xdai":"xdai","arbitrum-one":"arbitrum_one","base":"base","bnb":"bnb","polygon":"polygon","avalanche":"avalanche","linea":"linea","ink":"ink","plasma":"plasma"}
UA={"User-Agent":"Mozilla/5.0"}
total=collections.Counter(); okc=collections.Counter(); bad=[]; apierr=0
for c,cid in CHAIN_ID.items():
    a=fetch(c,ids[c][-1]); dom=TypedDataDomain("Gnosis Protocol","v2",cid,SETTLEMENT)
    for o in a.get("orders",[]):
        scheme=o.get("signingScheme"); total[(c,scheme)]+=1
        # first pass with DTO fields
        def build(src, amounts):
            rec=src.get("receiver") or ""
            if rec and int(rec,16)==0: rec=""
            return Order(sell_token=Web3.to_checksum_address(src["sellToken"]),buy_token=Web3.to_checksum_address(src["buyToken"]),receiver=Web3.to_checksum_address(rec) if rec else "",
                sell_amount=str(amounts[0]),buy_amount=str(amounts[1]),valid_to=src["validTo"],app_data=src["appData"],fee_amount=str(amounts[2]),kind=src["kind"],
                partially_fillable=src["partiallyFillable"],sell_token_balance=src.get("sellTokenSource",src.get("sellTokenBalance","erc20")),buy_token_balance=src.get("buyTokenDestination",src.get("buyTokenBalance","erc20")))
        def check(od):
            uid=compute_order_uid(dom,od,Web3.to_checksum_address(o["owner"])).lower()
            if uid!=o["uid"].lower(): return False
            if scheme in ("eip712","ethsign"):
                d=bytes(hash_order(dom,od)); d=keccak(PREFIX+d) if scheme=="ethsign" else d
                return Account._recover_hash(d,signature=o["signature"]).lower()==o["owner"].lower()
            return True
        ok=check(build(o,(o.get("fullSellAmount",o["sellAmount"]),o.get("fullBuyAmount",o["buyAmount"]),"0")))
        if not ok:
            try:
                time.sleep(0.15)
                full=json.load(urllib.request.urlopen(urllib.request.Request(f"https://api.cow.fi/{API[c]}/api/v1/orders/{o['uid']}",headers=UA),timeout=60))
                ok=check(build(full,(full["sellAmount"],full["buyAmount"],full["feeAmount"])))
                if not ok: bad.append((c,o["uid"],scheme,full["feeAmount"],full.get("class")))
            except Exception as e:
                apierr+=1; bad.append((c,o["uid"],scheme,"APIERR",str(e)[:60]))
        if ok: okc[(c,scheme)]+=1
print("chain/scheme totals vs ok:")
for k in sorted(total): print(f"  {k[0]:13}{str(k[1]):9} {okc[k]:5}/{total[k]}")
print("TOTAL", sum(okc.values()),"/",sum(total.values()),"api errors",apierr)
print("remaining mismatches:",len(bad)); [print("  ",b) for b in bad[:30]]
