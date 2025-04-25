import time
from fetch_proxies import fetch_proxy_list
from check_proxies import check_proxy

class ProxyManager:
    def __init__(self):
        self.valid_proxies = []

    def update_proxies(self):
        print("\n Updating proxy list...")
        new_proxies = fetch_proxy_list()
        print(f"{len(new_proxies)} proxies captured, testing in progress...")
        valid = []
        for proxy in new_proxies:
            if check_proxy(proxy):
                valid.append(proxy)
        self.valid_proxies = valid
        print(f"Detection completed, current number of available proxies: {len(self.valid_proxies)}")
        self.save_proxies()

    def save_proxies(self):
        with open("proxies_valid.txt", "w") as f:
            for proxy in self.valid_proxies:
                f.write(proxy + "\n")

    def run(self, interval=900):
        while True:
            self.update_proxies()
            print(f"Rest for{interval}seconds before continuing to update...")
            time.sleep(interval)
