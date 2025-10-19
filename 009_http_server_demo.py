# http_server_demo.py - 带 API 接口的简易服务器
import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler


# 定义继承自SimpleHTTPRequestHandler的类
class CustomHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # 这里可以自定义格式
        print(f"[{self.log_date_time_string()}] {self.client_address[0]} "
              f"{self.command} {self.path} -> {format % args}")
    def do_GET(self):
        """重写 GET 方法，实现自定义 API"""
        if self.path.startswith('/api/'):
            # 自定义 API 返回内容
            response_data = {
                "status": "ok",
                "path": self.path,
                "message": "这是自定义 API 返回的内容",
                "User-Agent": self.headers["User-Agent"]
            }

            # 设置响应头
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(response_data, ensure_ascii=False, indent=2).encode("utf-8"))
        else:
            # 不是 API 请求，则回退到静态文件处理
            super().do_GET()


def apiServer(host='', port=8000, directory=None):
    addr = (host, port)
    directory = directory or os.getcwd()
    # 使用lambda定义一个自定义匿名函数
    # 相当于
    # def handler_class(*args, **kwargs):
    #     return CustomHandler(*args, directory=directory, **kwargs)
    handler_class = lambda *args, **kwargs: CustomHandler(*args, directory=directory, **kwargs)

    print(f"启动 API+静态文件服务器：http://{host}:{port}")
    print(f"静态文件路径：{directory}")
    print("API 示例：http://{}/api/test".format(f"{host}:{port}"))

    HTTPServer(addr, handler_class).serve_forever()


if __name__ == '__main__':
    apiServer("127.0.0.1", 8081, "D:/Desktop")
