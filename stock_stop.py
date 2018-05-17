import requests, json

list_stock = [
    "XAUUSD",
    "XAGUSD",
    "XPTUSD",
    "XPDUSD",
    "COPPER",
    "UKOIL",
    "USOIL",
    "USDOLLARINDEX",
    "EURUSD",
    "NGAS",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCHF",
    "NZDUSD",
    "USDCNH",
    "US30INDEX",
    "NASINDEX",
    "SPX500INDEX",
    "JPN225INDEX",
    "000001",
    "399001"]
d = dict()
for i in list_stock:
    url = f"http://demo-finance.api51.cn/api/r.php?en_prod_code={i}"
    d[i] = json.loads(requests.get(url).content.decode()).get("data").get('snapshot').get(i)[6]

print(d)
ff = json.dumps(d)
# f = open('o.json', 'w')
# f.write(ff)
