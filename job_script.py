import socket

# 監視したいURLのリスト
urls = [
    "ytas.obc-service.biz",
    "support.obc.jp",
    "obc3342.rohd.jp",
    "www.obcnet.jp",
    "mynapf.nta.go.jp",
    "app.api.myna.go.jp",
    "mcss.obc-service.biz",
    "mcss-auth.obc-service.biz",
    "id.obc.jp",
    "hromssp.obc.jp",
    "authnsrv.obc-service.biz"
]

results = {}
for url in urls:
    try:
        ip_address = socket.gethostbyname(url)
        results[url] = ip_address
    except socket.gaierror:
        results[url] = "Could not resolve the IP address"

# 結果をコンソールに出力
print(results)