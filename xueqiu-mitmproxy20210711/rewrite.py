import json

import mitmproxy.http
from mitmproxy import http, ctx


class Rewrite:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 给定监听的url匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url \
                and "x=" in flow.request.pretty_url:
            ctx.log.info(f"{flow.response.text}")
            # 使用json的loads方法转为字典格式
            data = json.loads(flow.response.text)
            # 修改股价变颜色
            data["data"]["items"][0]["quote"]["current"] = "-0.00000001"
            data["data"]["items"][1]["quote"]["current"]="0"
            data["data"]["items"][2]["quote"]["current"] = "999999999"
            data["data"]["items"][3]["quote"]["current"] = "-999999999"
            data["data"]["items"][0]["quote"]["percent"] = "-0.00000001"
            data["data"]["items"][1]["quote"]["percent"] = "0"
            data["data"]["items"][2]["quote"]["percent"] = "999999999"
            data["data"]["items"][3]["quote"]["percent"] = "-999999999"
            # 修改响应后返回
            flow.response.text = json.dumps(data)


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])

