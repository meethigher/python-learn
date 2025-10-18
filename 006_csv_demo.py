# csv_demo.py - csv 读写
import csv
import os

if __name__ == '__main__':
    rows = [['name', 'age'], ['alice', '30'], ['bob', '25']]
    with open('demo.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print('写入 demo.csv')
    with open('demo.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # 逐行读取
        for r in reader:
            print('读取行:', r)

    os.remove('demo.csv')
