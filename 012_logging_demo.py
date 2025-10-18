# logging_demo.py - logging 配置与使用
import logging

logging.basicConfig(
    level=logging.DEBUG,
    # %-8.8s 左对齐，宽度 8，最多 8 个字符
    # %8.8s 右对齐，宽度 8，最多 8 个字符
    # %.8s 默认左对齐，最多 8 个字符，不填充空格
    format='%(asctime)s - %(levelname)-8.8s - [%(threadName)12.12s] - [%(funcName)-12.12s] - %(message)s',
)


def main():
    logger = logging.getLogger('demo')
    logger.debug('调试信息')
    logger.info('普通信息')
    logger.warning('警告信息')


if __name__ == '__main__':
    main()
