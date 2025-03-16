def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # yield 返回一个值，并且暂停函数执行，直到下一次调用时继续
        count += 1

gen = count_up_to(5)
for num in gen:
    print(num)  # 输出 1, 2, 3, 4, 5，每次调用时返回一个值