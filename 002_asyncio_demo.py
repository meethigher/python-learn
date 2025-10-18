# asyncio_demo.py - 基本 asyncio 用法
# https://docs.python.org/zh-cn/3.11/library/asyncio-task.html
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def create_multi_task():
    task1 = asyncio.create_task(say_after(1, 'multi_halo'))

    task2 = asyncio.create_task(say_after(2, 'multi_wode'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
    return "finished"


async def main():
    await say_after(1, "hello")
    await say_after(0.5, "world")
    print(await create_multi_task())

    # 并发执行多个任务
    tasks = [
        say_after(1, "async_hello"),
        say_after(1, "async_world"),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # asyncio.run() 函数用来运行最高层级的入口点
    asyncio.run(main())
