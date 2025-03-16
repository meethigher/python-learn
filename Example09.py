# 引入其他模块写的函数
from sub09.func.Sub09Func import print_info
# 引入其他模块定义的类
from sub09.clazz.Sub09Class import Animal

animal = Animal("HK")

content = animal.speek()

print_info(speek=content)
