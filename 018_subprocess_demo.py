# subprocess_demo.py - 启动外部进程（示例，不会注入用户输入）
import subprocess, sys

def main():
    res = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)
    print('python --version 输出:', res.stdout.strip() or res.stderr.strip())

if __name__ == '__main__':
    main()
