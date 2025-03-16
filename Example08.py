# 读文件
with open('python-learn.md', 'r', encoding='utf-8') as f:
    content = f.read()  # 一次性读取整个文件内容
    print(content)

# 写文件
with open('output.sh', 'w', encoding='utf-8') as f:
    f.write("Hello, Python!")  # 将文本写入文件
