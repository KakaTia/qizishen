import json

import mitmproxy.http
from mitmproxy import http, ctx


class MapLocal_modifyname:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 给定监听的url匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url\
                and "x=" in flow.request.pretty_url:
            # 打开本地文件
            with open("data.json", encoding="utf-8") as f:
                # 制造响应体
                flow.response = http.HTTPResponse.make(
                    # 状态码响应
                    200,
                    # 数据体
                    f.read(),

                )



addons = [
    MapLocal_modifyname()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
