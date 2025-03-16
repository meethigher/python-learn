try:
    x = 10 / 0  # 这里会抛出 ZeroDivisionError 异常，因为除数是 0
except ZeroDivisionError as e:
    print("除数不能为零")
else:
    print("没有异常发生")
finally:
    print("无论如何都会执行")
