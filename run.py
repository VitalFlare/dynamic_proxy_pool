from proxy_manager import ProxyManager

if __name__ == "__main__":
    pm = ProxyManager()
    pm.run(interval=1800)  # 每半小时更新一次（1800秒）