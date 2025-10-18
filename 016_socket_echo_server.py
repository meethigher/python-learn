# socket_echo_server.py - 简单 TCP 回显服务器示例（注意：运行会阻塞并绑定端口）
import socket

def run_server(host='127.0.0.1', port=9001):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f'回显服务器监听 {host}:{port}（按 Ctrl-C 停止）')
        conn, addr = s.accept()
        with conn:
            print('连接来自', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == '__main__':
    print('这是示例文件；请谨慎运行。')
