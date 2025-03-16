class Dog:
    def __init__(self, name, age):
        # __init__ 是构造函数，用于初始化类实例
        # self 表示实例本身，name 和 age 是对象的属性
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")


dog1 = Dog("Buddy", 3)
dog1.bark()  # 输出 "Buddy is barking!"


# 单继承
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")


cat = Cat("Tom")
cat.eat()  # 继承自 Animal 类的方法
cat.meow()  # 自身的方法


# 多继承
class Flyable:
    def fly(self):
        print("Flying...")


class Swimmable:
    def swim(self):
        print("Swimming...")


class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")


duck = Duck()
duck.fly()
duck.swim()
duck.quack()


# 方法重写
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shapes = [Circle(5), Rectangle(3, 4)]
for shape in shapes:
    print(shape.area())


# 魔法方法
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __add__(self, other):
        return f"self={self.title}, other={other.title}"

    def __len__(self):
        return len(self.title)


book = Book("Python Crash Course", "Eric Matthes")
print(book)  # 调用 __str__ 方法
print(repr(book))  # 调用 __repr__ 方法
print(len(book))  # 调用 __len__ 方法

a = Book("a", "a")
b = Book("b", "b")
print(a + b)  # 调用 a+b 实际上，是触发了 a.__add__(b) 的方法



# 类属性和实例属性
class Car:
    # 类属性
    wheels = 4

    def __init__(self, brand):
        # 实例属性
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels)  # 访问类属性
print(car1.brand)   # 访问实例属性

Car.wheels = 6  # 修改类属性
print(car2.wheels)  # 所有实例的类属性都被修改