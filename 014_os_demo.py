# os_demo.py - 演示 os 模块文件与目录操作
import os
from pathlib import Path

def main():
    print('当前工作目录:', os.getcwd())
    p = Path('demo_tmp_dir')
    p.mkdir(exist_ok=True)
    (p / 'hello.txt').write_text('hello from os_demo')
    print('创建文件:', p / 'hello.txt')
    for name in os.listdir(p):
        print('目录内容:', name)
    # 清理
    (p / 'hello.txt').unlink()
    p.rmdir()
    print('已清理 demo_tmp_dir')

if __name__ == '__main__':
    main()
