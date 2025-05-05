import urllib.request

def check_proxy(ip_port):
    proxy_handler = urllib.request.ProxyHandler({
        "http": f"http://{ip_port}",
        "https": f"http://{ip_port}"
    })
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)

    req = urllib.request.Request("https://httpbin.org/ip", headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) obsidian/1.8.4 Chrome/130.0.6723.191 Electron/33.3.2 Safari/537.36'
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
