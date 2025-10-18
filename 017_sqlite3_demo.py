# sqlite3_demo.py - sqlite3 使用示例
import sqlite3

def main():
    conn = sqlite3.connect('demo.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS kv (k TEXT PRIMARY KEY, v TEXT)')
    cur.execute('INSERT OR REPLACE INTO kv (k, v) VALUES (?, ?)', ('hello', 'world'))
    conn.commit()
    for row in cur.execute('SELECT k, v FROM kv'):
        print('row:', row)
    conn.close()
    import os
    os.remove('demo.db')

if __name__ == '__main__':
    main()
