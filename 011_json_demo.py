# json_demo.py - json 编解码
import json

if __name__ == '__main__':
    data = {'name': '小明', 'age': 30, 'feeling':'😂', 'languages': ['python', 'go']}
    s = json.dumps(data, ensure_ascii=True, indent=2)
    print('JSON 字符串:')
    print(s)
    obj = json.loads(s)
    print('解析后对象:', obj)
