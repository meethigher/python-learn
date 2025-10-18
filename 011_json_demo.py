# json_demo.py - json 编解码
import json
data = {'name': 'alice', 'age': 30, 'languages': ['python', 'go']}
s = json.dumps(data, ensure_ascii=False, indent=2)
print('JSON 字符串:')
print(s)
obj = json.loads(s)
print('解析后对象:', obj)
