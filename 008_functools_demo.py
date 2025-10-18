# functools_demo.py - lru_cache, partial, wraps
import logging
import time
from functools import lru_cache, partial

logging.basicConfig(
    level=logging.DEBUG,
    # %-8.8s 左对齐，宽度 8，最多 8 个字符
    # %8.8s 右对齐，宽度 8，最多 8 个字符
    # %.8s 默认左对齐，最多 8 个字符，不填充空格
    format='%(asctime)s - %(levelname)-8.8s - [%(threadName)12.12s] - [%(funcName)-12.12s] - %(message)s',
)


# lru_cache 是 Least Recently Used 缓存，用于给函数加缓存
#
# 作用：记住函数最近调用的结果，避免重复计算
#
# maxsize=32 表示缓存最多 32 个不同参数的结果
@lru_cache(maxsize=3)
def sleep(n):
    logging.info(f"start sleep {n}")
    time.sleep(n)
    logging.info(f"end sleep {n}")
    return n


def add(a, b):
    return a + b


# partial可以将一个函数的部分参数固定，然后返回一个新函数
def partial_add():
    add3 = partial(add, 3)
    print(add3(2))

    addLambda = lambda a, b: a + b
    print(addLambda(4, 5))
    add3Lambda = partial(addLambda, 3)
    print(add3Lambda(2))


if __name__ == '__main__':
    partial_add()

    print(sleep(1))
    print(sleep(2))
    print(sleep(3))
    print(sleep(1))
    print(sleep(2))
    print(sleep(3))
