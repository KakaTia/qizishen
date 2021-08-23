import logging
from api.base_API import BaseAPI

class Contactpage(BaseAPI):

    def create(self):
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": 1
        }
        logging.info(f"发送post请求-创建{data['name']}成员")
        r= self.send("post", f"user/create?access_token={self.token}", json=data)

        return r

    def modify(self):
        data = {
            "userid": "zhangsan",
            "name": "李四",
            "mobile": "+86 13800000000",
            "department": 1

        }
        logging.info(f"发送post请求-更新id为{data['userid']}的{data['name']}成员的名字")
        r = self.send("post", f"user/update?access_token={self.token}", json=data)
        return r

    def get(self):
        data = "zhangsan"
        logging.info(f"发送post请求-获取id为{data}的成员信息")
        r = self.send("post", f"user/get?access_token={self.token}&userid={data}")
        return r

    def delete(self):
        data = "zhangsan"
        logging.info(f"发送post请求-删除id为{data}的成员信息")
        r = self.send("post",f"user/delete?access_token={self.token}&userid={data}")
        return r