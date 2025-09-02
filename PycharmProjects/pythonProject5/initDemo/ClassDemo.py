#python类中不是this而是self（区别于其它语言）
# 通过实例对象调用方法时会自动将这个实例对象传递给参数表中的self，而用类调用则不会
# def __init__(self)表示类的构造方法
# def __del__(self)表示类的析构方法
# def __str__(self)表示类的字符串化方法，用于打印和比较大小
#以下是用于比较的六个核心方法：
 # 1. `__lt__(self, other)`: 实现小于运算符（<）。
 # 2. `__le__(self, other)`: 实现小于等于运算符（<=）。
 # 3. `__eq__(self, other)`: 实现等于运算符（==）。
 # 4. `__ne__(self, other)`: 实现不等于运算符（!=）。在Python 3中，如果定义了`__eq__`，则`__ne__`默认会调用`__eq__`并取反，但也可以自定义行为。
 # 5. `__gt__(self, other)`: 实现大于运算符（>）。
 # 6. `__ge__(self, other)`: 实现大于等于运算符（>=）。
#使用@classmethod注解表示定义的是类的方法，默认传入的第一个参数是类，第二个开始才是调用函数时传入的参数
#使用@staticmethod注解表示定义的是类的静态方法，没有默认传入的参数，第一个开始就是调用函数时传入的参数

# 若使用del函数删除对象时，若已无指针指向这片内存空间，则会自动销毁（执行析构函数）
# 私有属性会被解释器自动重命名为 _类名__属性名 的形式，可通过改写后的名称直接访问：

class MyClass:
    def __init__(self):
        self.__private_attr = 42  # 私有属性

obj = MyClass()
print(obj._MyClass__private_attr)  # 输出: 42

# 使用 property 装饰器（优雅方案）
class MyClass:
    def __init__(self):
        self.__private_attr = 42

    @property
    def private_attr(self):  # Getter
        return self.__private_attr

    @private_attr.setter
    def private_attr(self, value):  # Setter
        self.__private_attr = value


obj = MyClass()
print(obj.private_attr)  # 输出: 42 (像访问公有属性一样)
obj.private_attr = 100  # 直接赋值






# 以下是一个简单的Python多继承示例，包含两个父类和一个子类，展示了方法继承和调用顺序：
# 定义第一个父类
class Father:
    def __init__(self):
        self.father_name = "张伟"

    def show_father(self):
        print(f"父亲: {self.father_name}")


# 定义第二个父类
class Mother:
    def __init__(self):
        self.mother_name = "李芳"

    def show_mother(self):
        print(f"母亲: {self.mother_name}")

    def common(self):
        print("调用母类共同方法")


# 子类同时继承两个父类
class Child(Father, Mother):
    def __init__(self, name):
        # 显式调用父类初始化方法
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = name

    def show_child(self):
        print(f"孩子: {self.child_name}")

    def common(self):
        print("调用子类重写方法")

    def introduce(self):
        self.show_father()  # 继承自Father
        self.show_mother()  # 继承自Mother
        self.show_child()
        self.common()  # 调用子类重写方法
        Mother.common(self)  # 显式调用母类方法


# 创建子类实例
child = Child("小明")

# 调用方法
child.introduce()

# 查看方法解析顺序(MRO)
print("\n方法解析顺序(MRO):", Child.mro())
# 方法解析顺序(MRO)：使用Child.mro()查看继承顺序（深度优先，从左到右）

#在Python中，`isinstance()`和`issubclass()`是两个用于检查对象与类之间关系的内置函数。
# 1. `isinstance(object, classinfo)`:
#    - 用于检查一个对象是否是指定类或元组中任意一个类的实例。
#    - 如果`object`是`classinfo`的实例，或者其子类的实例，则返回`True`，否则返回`False`。
# 2. `issubclass(class, classinfo)`:
#    - 用于检查一个类是否是另一个类的子类（派生类）。
#    - 如果`class`是`classinfo`的子类（或者`classinfo`是一个元组，则检查是否是元组中任意一个类的子类），则返回`True`，否则返回`False`。
#    - 注意：每个类都被认为是自己的子类。
#   -type可获得对象所属的类

# 在 Python 中，类可以在创建后动态地添加或修改属性和方法。这种灵活性是 Python 动态特性的重要体现。
class Person:
    def __init__(self, name):
        self.name = name

# 创建实例
p = Person("张三")

# 1. 动态添加实例方法
def say_hello(self):
    print(f"{self.name}说：你好！")

p.greet = say_hello  # 直接添加到实例
p.greet(p)  # 需要手动传入self

# 更好的方式：使用MethodType绑定实例
from types import MethodType
p.greet = MethodType(say_hello, p)
p.greet()  # 正确调用：张三说：你好！

# 2. 动态添加类方法（所有实例共享）
def introduce(self):
    print(f"我是{self.name}，很高兴认识你！")

Person.introduce = introduce  # 添加到类

p2 = Person("李四")
p2.introduce()  # 我是李四，很高兴认识你！
p.introduce()   # 我是张三，很高兴认识你！

# 3. 动态添加属性
p.age = 30
print(f"{p.name}的年龄是{p.age}岁")  # 张三的年龄是30岁

# 4. 动态添加静态方法
@staticmethod
def class_info():
    print("这是一个Person类")

Person.info = class_info
Person.info()  # 这是一个Person类

# __slots__：限制动态属性
# __slots__ 是一个类变量，用于限制实例可以拥有的属性，主要目的是：
#
# 节省内存：避免每个实例都创建 __dict__
#
# 提高属性访问速度
#
# 防止动态添加属性

class Point:
    __slots__ = ('x', 'y')  # 只允许这两个属性

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.x, p.y)  # 3 4

# 尝试添加新属性会失败
try:
    p.z = 5
except AttributeError as e:
    print(f"错误: {e}")  # 'Point' object has no attribute 'z'

# 继承中的 __slots__
class Base:
    __slots__ = ('a',)


class Derived(Base):
    __slots__ = ('b',)  # 扩展基类的slots


d = Derived()
d.a = 1
d.b = 2
print(d.a, d.b)  # 1 2


# 如果子类不定义__slots__，则会有__dict__
class NoSlots(Base):
    pass


ns = NoSlots()
ns.a = 1
ns.c = 3  # 可以动态添加属性
print(ns.c)  # 3