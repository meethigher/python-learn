x = 10  # 整数
y = 3.14  # 浮点数
name = "Alice"  # 字符串
is_active = True  # 布尔值

# 切片
s = "Hello, World!"
print(s[0:5])  # 输出 "Hello"
print(s[7:])   # 输出 "World!"

# 拼接
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # 输出 "Hello World"

# 格式化方法
name = "Alice"
age = 25
# 旧式格式化
print("My name is %s, and I am %d years old." % (name, age))
# 新式格式化
print("My name is {}, and I am {} years old.".format(name, age))
# f-string 格式化
print(f"My name is {name}, and I am {age} years old.")


# 增
my_list = [1, 2, 3]
my_list.append(4)  # 在列表末尾添加元素
print(my_list)  # 输出 [1, 2, 3, 4]
my_list.insert(1, 5)  # 在指定位置插入元素
print(my_list)  # 输出 [1, 5, 2, 3, 4]

# 删
my_list.pop()  # 删除列表末尾元素
print(my_list)  # 输出 [1, 5, 2, 3]
my_list.remove(5)  # 删除指定元素
print(my_list)  # 输出 [1, 2, 3]

# 改
my_list[1] = 10  # 修改指定位置元素
print(my_list)  # 输出 [1, 10, 3]

# 查
print(my_list.index(10))  # 查找元素位置，输出 1

# 排序
my_list = [3, 1, 2]
my_list.sort()  # 升序排序
print(my_list)  # 输出 [1, 2, 3]
my_list.sort(reverse=True)  # 降序排序
print(my_list)  # 输出 [3, 2, 1]

# 键值对操作
my_dict = {'name': 'Alice', 'age': 25}
# 增/改
my_dict['city'] = 'New York'  # 添加新的键值对
my_dict['age'] = 26  # 修改已有键的值
print(my_dict)  # 输出 {'name': 'Alice', 'age': 26, 'city': 'New York'}

# 删
del my_dict['city']  # 删除指定键值对
print(my_dict)  # 输出 {'name': 'Alice', 'age': 26}

# 查
print(my_dict.get('name'))  # 获取指定键的值，输出 'Alice'

# 条件语句
age = 18
if age < 18:
    print("未成年")
elif age == 18:
    print("刚成年")
else:
    print("成人")

# 循环
# 定义循环次数的变量
num_iterations = 5

# for 循环
for i in range(num_iterations):
    print(i)

# while 循环
i = 0
while i < num_iterations:
    print(i)
    i += 1

# 输出单个字符串
print("Hello, Python!")

# 输出多个参数
x = 10
y = 3.14
print("x =", x, "y =", y)

# 格式化输出
name = "Alice"
age = 25
print(f"My name is {name}, and I am {age} years old.")