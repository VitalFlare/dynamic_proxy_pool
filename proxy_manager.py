import time
from fetch_proxies import fetch_proxy_list
from check_proxies import check_proxy

class ProxyManager:
    def __init__(self):
        self.valid_proxies = []

    def update_proxies(self):
        print("\n正在更新代理列表...")
        new_proxies = fetch_proxy_list()
        print(f"抓取到 {len(new_proxies)} 个代理，正在检测...")
        valid = []
        for proxy in new_proxies:
            if check_proxy(proxy):
                valid.append(proxy)
        self.valid_proxies = valid
        print(f"检测完毕，目前可用代理数量: {len(self.valid_proxies)}")
        self.save_proxies()

    def save_proxies(self):
        with open("proxies_valid.txt", "w") as f:
            for proxy in self.valid_proxies:
                f.write(proxy + "\n")

    def run(self, interval=1800):
        while True:
            self.update_proxies()
            print(f"休息 {interval} 秒后继续更新...")
            time.sleep(interval)