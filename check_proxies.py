import urllib.request

def check_proxy(ip_port):
    proxy_handler = urllib.request.ProxyHandler({
        "http": f"http://{ip_port}",
        "https": f"http://{ip_port}"
    })
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    req = urllib.request.Request("https://httpbin.org/ip", headers={
        "User-Agent": "Mozilla/5.0"
    })

    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"[√] valid proxy: {ip_port}")
            with open('proxies_valid.txt','a') as f:
                f.write(ip_port + "\n")
            return True
    except:
        print(f"[×] invalid proxy: {ip_port}")
        return False
