# http_server_demo.py - 简单的静态文件服务器示例（基于 http.server）
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


def run(host='', port=8000, directory=None):
    addr = (host, port)
    directory = directory or os.getcwd()
    handler_class = lambda *args, **kwargs: SimpleHTTPRequestHandler(*args, directory=directory, **kwargs)

    print(f"启动静态文件服务器 http://{host}:{port} 静态文件路径 {directory}")
    HTTPServer(addr, handler_class).serve_forever()


if __name__ == '__main__':
    run("127.0.0.1", 8081, "D:/Desktop")
