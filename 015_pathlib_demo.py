# pathlib_demo.py - Path 用法
from pathlib import Path

def main():
    p = Path('.')
    print('当前目录下的 py 文件：')
    for f in p.glob('*.py'):
        print('-', f.name)
    tmp = Path('example_dir')
    tmp.mkdir(exist_ok=True)
    print('创建目录:', tmp.resolve())
    # 清理
    tmp.rmdir()

if __name__ == '__main__':
    main()
