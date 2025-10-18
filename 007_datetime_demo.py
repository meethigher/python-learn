# datetime_demo.py - datetime 使用
from datetime import datetime, timedelta, timezone

def main():
    now = datetime.now()
    print('当前本地时间:', now)
    print(now.strftime("%Y-%m-%d %H:%M:%S,%f"))
    print(now.strftime("%Y/%m/%d %I:%M %p"))
    print(now.strftime("%a, %b %d, %Y"))

    utc = datetime.utcnow().replace(tzinfo=timezone.utc)
    print('UTC 时间:', utc)
    print('时间加减:', now + timedelta(days=1, hours=2))

if __name__ == '__main__':
    main()
