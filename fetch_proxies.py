import requests
from bs4 import BeautifulSoup

def fetch_proxy_list():
    url = "https://free-proxy-list.net/"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) obsidian/1.8.4 Chrome/130.0.6723.191 Electron/33.3.2 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        proxies = []
        for row in soup.select("table tbody tr")[:50]:
            cols = row.find_all("td")
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            https = cols[6].text.strip()
            if https == "yes":
                proxies.append(f"{ip}:{port}")
        return proxies
    except Exception as e:
        print(f"Fetching proxy failed: {e}")
        return []
