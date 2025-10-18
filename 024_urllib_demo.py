# urllib_demo.py - urllib.request 简单请求示例
import urllib.request

def main():
    url = 'http://httpbin.org/get'
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            print('状态码:', r.status)
            print('响应头示例:', dict(r.getheaders()) )
    except Exception as e:
        print('请求失败（在无网络环境下可能会失败）:', e)

if __name__ == '__main__':
    main()
