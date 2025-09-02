import copy

n1,n2=1,1
print("n1,n2的内存地址为",id(n1),id(n2));
# 整型数只要值一样地址就一样
# 字符串只要值一样地址就一样
t1,t2=(1,2,3),(1,2,3)
print("t1,t2的内存地址为",id(t1),id(t2));
# 元组值一样地址就一样（新版是这样，旧版不是这样）,对不可变类型整体重新赋值等于创建新的变量，内存地址会变化
ls1,ls2=[1,2,3],[1,2,3]
print("ls1,ls2的内存地址为",id(ls1),id(ls2));
# 列表值一样地址就一样，改变某个元素的值内存地址不变，对可变类型整体重新赋值等于创建新的变量，内存地址会变化
# 使用list方法创建列表对象，传入的参数是元组
# ls.index用于查找列表元素，ls.insert(index,x)用于插入，ls.append(x)用于末尾插入，ls.del用于删除
#可使用copy模块中的deepcopy函数，实现列表复制操作
#可使用max，min直接获取最大、最小元素，count用于统计某个元素出现的次数，len用于获取列表长度
#sort函数接收两个参数，第一个参数用于接收一个函数用于定义比较规则，第二个参数表示按升序还是降序（0，1）

# tuple和（）都可创建元组
#创建单元素元组要用（1，）末尾要加一个逗号，不然会认为是整型

#set（列表），和{}都可以创建集合，但{}不饿能创建空列表，否则会被认为是一个空字典，add用于插入可哈希对象，update（x）将x拆分成多个元素对象再插入，因此x需要是可迭代对象，两个都为末尾插入

#集合运算api
#intersection计算交集，union用于fan'hui并集，s1.difference(s2)计算差集（只包含在s1中），s1.symmetric_difference(s2)计算只包含s1和s2的元素
#上述方法都返回一个集合
#子集和父集的判断：issubset子集判断，issuperset父集判断，判断是对于调用者而言

#字典创建：dict函数或{}，实质上是键值对组成的数组
#fromkeys用于初始化字典，如果原有其他元素，调用该方法时原有元素都会被清除
#update函数用于一次性修改或插入多个元素，传入的参数可为另一个字典对象或多个键值对（key=value...）
# 在 Python 字典中，del 和 pop() 都用于删除键值对，但用法和特性有重要区别：
#
# 1. del 语句
# 功能：直接删除指定键的键值对（无返回值）
# 语法：del dict[key]
# 特点：
# 键必须存在，否则抛出 KeyError
# 不返回被删除的值
# 支持删除整个字典（del dict）
person = {"name": "Alice", "age": 30, "city": "Paris"}

# 删除键 "age"
del person["age"]
print(person)  # 输出: {'name': 'Alice', 'city': 'Paris'}

# 尝试删除不存在的键 → 报错
# del person["salary"]  # KeyError: 'salary'

# 2. pop() 方法
# 功能：删除指定键并返回对应的值
# 语法：dict.pop(key[, default])
# 特点：
# 可设置默认值 default（避免 KeyError）
# 必须传入键名（不能省略参数）
# 返回被删除的值

person = {"name": "Bob", "age": 25, "city": "London"}

# 删除键 "age" 并返回值
age = person.pop("age")
print(age)     # 输出: 25
print(person)  # 输出: {'name': 'Bob', 'city': 'London'}

# 安全删除：键不存在时返回默认值
salary = person.pop("salary", 0)  # 无 "salary" 键 → 返回 0
print(salary)  # 输出: 0

# 不设默认值且键不存在 → 报错
# person.pop("salary")  # KeyError: 'salary'


# 字典的copy方法是浅拷贝
# copy.deepcopy()用于深拷贝

#判断字典中是否存在某个键，字典.get（键值）方法，in方法： 键值 in 字典
#拼接方法：
# 1. 使用 update() 方法
# 特点：
# 原地修改原字典
# 重复键的值会被覆盖
# 支持合并多个字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)  # 输出: {'a': 1, 'b': 3, 'c': 4}

# 合并多个字典
dict3 = {"d": 5}
dict1.update(dict2, **dict3)  # 或 dict1.update({**dict2, **dict3})

# 2. 字典解包 (Python 3.5+)
# 特点：
# 创建新字典，不修改原字典
# 重复键的值以后面的字典为准
# 最简洁的合并方式
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)  # 输出: {'a': 1, 'b': 3, 'c': 4}

# 合并多个字典
dict3 = {"d": 5}
merged_dict = {**dict1, **dict2, **dict3}

# 3. 合并运算符 | (Python 3.9+)
# 特点：
# 专为字典合并设计的运算符
# 可读性高
# 支持 |= 原地合并

dict1 = {"a": 1}
dict2 = {"b": 2}

# 创建新字典
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2}

# 原地合并
dict1 |= dict2  # 等价于 dict1.update(dict2)

#字典中常用的操作：len、clear、keys（返回一个对象包含中的所有键）、values（同左）、items（返回一个可按（键，值）方式遍历的对象）

#切片
# 切片（Slicing）
# 用于从序列中提取子集，语法：sequence[start:stop:step]
# 参数说明
# start：起始索引（包含），默认为 0
# stop：结束索引（不包含），默认为序列末尾
# step：步长（默认为 1），负数表示反向切片
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基础切片
print(nums[2:5])     # [2, 3, 4]   (索引2到4)
print(nums[:3])      # [0, 1, 2]   (从头开始)
print(nums[5:])      # [5, 6, 7, 8, 9] (到末尾)

# 步长控制
print(nums[1:8:2])   # [1, 3, 5, 7] (步长为2)
print(nums[::3])     # [0, 3, 6, 9] (每隔3个取一个)

# 反向操作
print(nums[::-1])    # [9, 8, 7, ... 0] (反转列表)
print(nums[6:2:-1])  # [6, 5, 4, 3] (反向切片)

# 字符串切片
text = "Python"
print(text[1:4])     # "yth"

# 列表生成式（List Comprehensions）
# 用于快速创建/转换列表，语法：[expression for item in iterable if condition]
# 核心组件
# expression：对元素的处理表达式
# for 循环：遍历可迭代对象
# 条件过滤（可选）：if 语句筛选元素

# 基础创建
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 带条件过滤
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# 嵌套循环
matrix = [[1,2], [3,4], [5,6]]
flat = [num for row in matrix for num in row]  # [1,2,3,4,5,6]

# 复杂表达式
text = "Hello World"
vowels = [char.upper() for char in text if char.lower() in 'aeiou']  # ['E','O','O']

# 字典转换
prices = {'apple': 1.2, 'banana': 0.8}
discounted = [f"{k}: ${v*0.9:.2f}" for k, v in prices.items()]
# ['apple: $1.08', 'banana: $0.72']

#生成器
#创造生成器：
gen = (x for x in range(3))
# Python 生成器详解
# 生成器（Generator）是 Python 中一种特殊的迭代器，它可以按需生成值而不是一次性创建所有值，这在处理大数据集或无限序列时特别高效。
#
# 核心概念
# 1. 生成器 vs 普通函数
# 特性	普通函数	生成器函数
# 返回值	使用 return	使用 yield
# 执行状态	每次调用从头开始执行	保留上次执行状态
# 内存使用	一次性返回所有结果	按需生成值，节省内存
# 返回值类型	具体值	生成器对象
# 2. 创建生成器的两种方式
# (1) 生成器函数
# 使用 yield 关键字代替 return：


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# 使用生成器
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(list(counter))  # [3, 4, 5] (继续从上次状态)
# (2) 生成器表达式
# 类似列表推导式，但使用圆括号：


# 列表推导式 - 立即创建完整列表
squares_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 生成器表达式 - 按需生成值
squares_gen = (x**2 for x in range(5))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(list(squares_gen))  # [4, 9, 16] (剩余值)
# 生成器的工作原理
# 调用生成器函数时，返回生成器对象（不执行函数体）
#
# 首次调用 next() 时，执行到第一个 yield 语句暂停
#
# 再次调用 next() 时，从上次暂停处继续执行
#
# 遇到 return 或函数结尾时，抛出 StopIteration 异常


def generator_demo():
    print("开始执行")
    yield "第一步"
    print("继续执行")
    yield "第二步"
    print("结束执行")

gen = generator_demo()
print(next(gen))  # 输出: 开始执行 → 第一步
print(next(gen))  # 输出: 继续执行 → 第二步
print(next(gen))  # 抛出 StopIteration
# 生成器的核心特性
# 1. 惰性求值 (Lazy Evaluation)
# 值只在请求时生成
#
# 节省内存，特别适合大数据处理


# 生成无限序列
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

inf_gen = infinite_sequence()
print(next(inf_gen))  # 0
print(next(inf_gen))  # 1
# 不会耗尽内存，按需生成
# 2. 状态保持
# 局部变量在调用间保持状态
#
# 比类实现的迭代器更简洁


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13 21 34
# 3. 内存高效
# 比较处理大数据的资源消耗：


import sys

# 列表推导式
list_comp = [x for x in range(1000000)]
print(sys.getsizeof(list_comp))  # 约 8.5 MB

# 生成器表达式
gen_exp = (x for x in range(1000000))
print(sys.getsizeof(gen_exp))    # 约 128 字节

#可迭代对象：
# 能直接用for循环循环遍历的对象，可使用isinstance判断一个对象是否是可迭代对象
#对于可迭代对象，使用iter方法可以获取其迭代器
# 若要自定义迭代器，需要实现__next__和__iter__方法