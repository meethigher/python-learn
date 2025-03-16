# 线程
import threading

def print_numbers():
    for i in range(5):
        print(i)

# 创建两个线程
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print("thread1 and thread2 Done")

# 协程
import asyncio

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # 模拟 I/O 操作
    print("End")

# 创建事件循环并运行协程
asyncio.run(my_coroutine())