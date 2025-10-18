# sys_demo.py - 演示 sys.argv 与 sys.exit
import sys

def main():
    print('命令行参数:', sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == 'quit':
        print('收到 quit，退出并返回代码 2')
        sys.exit(2)
    print('正常结束')

if __name__ == '__main__':
    main()
