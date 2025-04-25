from proxy_manager import ProxyManager

if __name__ == "__main__":
    pm = ProxyManager()
    pm.run(interval=900)  # Update every 15 mins (900 seconds).
