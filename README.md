# dynamic_proxy_pool project(动态代理池项目)

# Project Overvie(项目简介)
This is a Python-based dynamic proxy pool project that fetches free proxy IPs and automatically checks their availability.
这是一个用 Python 编写的动态代理池项目，用于抓取免费的代理 IP，并自动验证其可用性。  

# Features(特色功能)
- Automatically fetch public proxy IPs (自动抓取公开代理）
- Validate proxy availability (验证代理有效性)
- Save valid proxies to `proxies_valid.txt` (将有效代理保存到 `proxies_valid.txt`)
- Update every 30 minutes (每30分钟自动更新一次)

dynamic_proxy_pool/
├── run.py                 # Main entry script / 程序主入口 
├── fetch_proxies.py       # Proxy fetcher module / 抓取代理 IP 的模块 
├── check_proxies.py       # Proxy checker / 检查代理是否可用 
├── proxy_manager.py       # Proxy pool manager / 管理代理池逻辑
├── proxies_valid.txt      # List of valid proxies / 可用代理列表 
└── README.md              # Project documentation / 项目说明文件

# Tech Stack (技术栈)
 • Python 3.x
 • requests / urllib
 • threading / 多线程

# Author (作者) 
 • VitalFlare
