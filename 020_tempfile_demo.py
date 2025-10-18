# tempfile_demo.py - 临时文件与临时目录示例
import tempfile
import os

def main():
    with tempfile.TemporaryDirectory() as td:
        print('临时目录:', td)
        fp = os.path.join(td, 't.txt')
        with open(fp, 'w') as f:
            f.write('temp data')
        print('文件已写入:', fp)
    print('临时目录已退出并删除')

if __name__ == '__main__':
    main()
