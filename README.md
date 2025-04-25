# dynamic_proxy_pool project(动态代理池项目)

# Project Overvie(项目简介)
This is a Python-based dynamic proxy pool project that fetches free proxy IPs and automatically checks their availability.
I created this project for the purpose of learning and practicing. you're welcome to make good use of this as your own target.
这是一个用 Python 编写的动态代理池项目，用于抓取免费的代理 IP，并自动验证其可用性。我创建这个项目的目的是为了学习和实践。欢迎您利用此作为您自己的用途。

# Features(特色功能)
- Automatically fetch public proxy IPs (自动抓取公开代理）
- Validate proxy availability (验证代理有效性)
- Save valid proxies to `proxies_valid.txt` (将有效代理保存到 `proxies_valid.txt`)
- Update every 15 minutes (每15分钟自动更新一次)

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

# How do I use these files? (该怎么用这些文件呢？)
This project is consisted of 4 python files. you can simply save these files into your IDE.
Run the 'run.py' file and you'll see valid proxies saved in the 'proxies_valid.txt' file.
此项目由4个python文件组成。只需将这些文件保存到你的开发环境中，再运行'run.py'的文件。
在这些Python代码的文件夹下你就会看到可用的IP代理和端口保存在 'proxies_valid.txt' 文件中。

# Author (作者) 
 • VitalFlare
