# multiprocessing_demo.py - 进程示例
import os
from multiprocessing import Process, Queue

def f(q, x):
    q.put(x * x)

def main():
    print('主进程 PID:', os.getpid())
    q = Queue()
    p = Process(target=f, args=(q, 5))
    p.start()
    print('子进程 PID:', p.pid)
    print('子进程计算结果:', q.get())
    p.join()

if __name__ == '__main__':
    main()
