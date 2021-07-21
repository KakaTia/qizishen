import requests

class BaseAPI:

    CORPID = "ww5de7673c8d85d97c"
    CORPSECRET = "KvCi9S-tNwOqpEmMqh3PScwQrsmZmwvXdKsoCJmiHZ0"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.token_corpid_corpsecret()

    def token_corpid_corpsecret(self):

     url = self.BASE_URL+f"/gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"
     r = requests.get(url)
     access_token = r.json().get("access_token")
     return access_token

    def send(self, method, url, **kwargs):
        url = self.BASE_URL + url
        "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN"
        # post 和 get 底层实现，requests.get == requests.request("GET",)
        return requests.request(method, url, **kwargs)
