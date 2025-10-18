# concurrent_futures_demo.py - 线程池/进程池示例
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.basicConfig(
    level=logging.DEBUG,
    # %-8.8s 左对齐，宽度 8，最多 8 个字符
    # %8.8s 右对齐，宽度 8，最多 8 个字符
    # %.8s 默认左对齐，最多 8 个字符，不填充空格
    format='%(asctime)s - %(levelname)-8.8s - [%(threadName)12.12s] - [%(funcName)-12.12s] - %(message)s',
)


def task(x):
    logging.info(f"start {x}")
    time.sleep(5)
    logging.info(f"end {x}")
    return x * x


def main():
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(task, i) for i in range(6)]
        logging.info(f"{len(futures)} task submitted")
        try:
            completed = as_completed(futures, timeout=1)
            for f in completed:
                logging.info(f"result: {f.result()}")
        except Exception as e:
            logging.error(e)
        logging.info("finished")


if __name__ == '__main__':
    main()
