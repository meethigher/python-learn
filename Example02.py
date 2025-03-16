def add(a, b=5):
    # 这里定义了一个函数 add，接收两个参数 a 和 b
    # b=5 是默认参数的写法，意思是如果调用函数时没有提供 b 的值，b 会默认为 5
    return a + b
print(add(10))  # 调用时只传递了 a，b 使用默认值 5 -> 10 + 5 = 15
print(add(10, 20))  # 调用时传递了 b，b 为 20 -> 10 + 20 = 30

# *args 用于接收任意数量的位置参数
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # 输出 6

# **kwargs 用于接收任意数量的关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

def add(a, b):
    return a + b

numbers = [1, 2]
print(add(*numbers))  # 参数解包，输出 3

info = {'a': 1, 'b': 2}
print(add(**info))  # 关键字参数解包，输出 3