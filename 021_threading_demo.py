# threading_demo.py - 线程示例
import threading, time

def worker(n):
    print(f'线程 {n} 启动')
    time.sleep(0.5)
    print(f'线程 {n} 结束')

def main():
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('所有线程完成')

if __name__ == '__main__':
    main()
