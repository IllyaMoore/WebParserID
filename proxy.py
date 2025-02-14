import requests

class Proxy:
    def __init__(self, ip: str, port: int, username: str = None, password: str = None):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def get_proxy_string(self):
        if self.username and self.password:
            return f"http://{self.username}:{self.password}@{self.ip}:{self.port}"
        return f"http://{self.ip}:{self.port}"

    def __repr__(self):
        auth = f"{self.username}:{self.password}@" if self.username else ""
        return f"<Proxy {auth}{self.ip}:{self.port}>"
    
proxy1 = Proxy(
    ip="198.23.239.134",
    port=6540,
    username="pozrzbkx",
    password="4mv7lp3tigi2"
)

proxy2 = Proxy(
    ip="207.244.217.165",
    port=6712,
    username="pozrzbkx",
    password="4mv7lp3tigi2"
)

proxy3 = Proxy(
    ip="107.172.163.27",
    port=6543,
    username="pozrzbkx",
    password="4mv7lp3tigi2"
)

proxy4 = Proxy(
    ip="64.137.42.112",
    port=5157,
    username="pozrzbkx",
    password="4mv7lp3tigi2"
)
