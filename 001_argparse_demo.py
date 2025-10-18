# argparse_demo.py - 命令行参数解析
import argparse

def main():
    p = argparse.ArgumentParser(description='示例 argparse')
    p.add_argument('--count', '-c', type=int, default=3, help='打印次数')
    p.add_argument('name', nargs='?', default='world', help='称呼')
    args = p.parse_args()
    for i in range(args.count):
        print(f'Hello, {args.name} (#{i+1})')

if __name__ == '__main__':
    main()
