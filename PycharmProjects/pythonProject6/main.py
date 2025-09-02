# str.strip();
# str.lstrip();
# str.rstrip();
#用于去除空格
#字符串中的大小写转换
# str.capitalize()第一个字母大写，其余小写
#str.lower(),str.upper()顾名思义
#str.swapcase()字符串的大写变小写，小写变大写

# 字符串是不可变类型，无法修改字符串中的某个元素值

#测试字符串的组成部分，find方法和in操作符

# Python 中的 join() 方法详解
# join() 是 Python 字符串对象的方法，用于将可迭代对象中的多个字符串元素连接成一个新的字符串。它是处理字符串拼接时最高效、最推荐的方法。
#
# 基本语法
# python
# new_string = separator.join(iterable)
# separator：连接元素时使用的分隔符（字符串）
#
# iterable：包含字符串元素的可迭代对象（列表、元组、集合、字符串等）
#
# 返回：由 iterable 中的元素连接而成的新字符串
#
# 核心特性
# 1. 基本用法
# python
# # 用空格连接
# words = ["Hello", "world", "!"]
# sentence = " ".join(words)
# print(sentence)  # 输出: Hello world !
#
# # 用逗号连接
# fruits = ["apple", "banana", "cherry"]
# csv_line = ",".join(fruits)
# print(csv_line)  # 输出: apple,banana,cherry
#
# # 无分隔符连接
# chars = ["P", "y", "t", "h", "o", "n"]
# word = "".join(chars)
# print(word)  # 输出: Python
# 2. 处理不同类型的数据
# python
# # 数字需要先转换为字符串
# numbers = [1, 2, 3]
# # num_str = ",".join(numbers)  # 会报错: TypeError
# num_str = ",".join(str(n) for n in numbers)
# print(num_str)  # 输出: 1,2,3
#
# # 混合类型处理
# data = ["ID", 123, 45.67, True]
# result = "|".join(str(item) for item in data)
# print(result)  # 输出: ID|123|45.67|True
# 3. 处理不同可迭代对象
# python
# # 元组
# colors = ("red", "green", "blue")
# print("-".join(colors))  # 输出: red-green-blue
#
# # 集合（无序）
# unique_chars = {"a", "b", "c"}
# print("".join(unique_chars))  # 输出可能是: acb（顺序不确定）
#
# # 字符串（每个字符作为元素）
# text = "hello"
# print(".".join(text))  # 输出: h.e.l.l.o
#
# # 字典（连接键）
# person = {"name": "Alice", "age": 30}
# print(";".join(person))  # 输出: name;age
# 性能优势
# join() 方法相比使用 + 运算符拼接字符串有显著的性能优势，特别是在处理大量字符串时：
#
# python
# import timeit
#
# # 使用 + 拼接
# def concat_plus():
#     s = ""
#     for i in range(10000):
#         s += str(i)
#     return s
#
# # 使用 join 拼接
# def concat_join():
#     parts = []
#     for i in range(10000):
#         parts.append(str(i))
#     return "".join(parts)
#
# # 性能测试
# print(timeit.timeit(concat_plus, number=100))   # 约 0.3-0.5 秒
# print(timeit.timeit(concat_join, number=100))   # 约 0.1-0.2 秒
# 性能差异原因：
#
# + 操作每次都会创建新字符串对象
#
# join() 预先计算总长度，一次性分配内存
#
# 高级用法
# 1. 多级连接
# python
# # 二维列表连接
# matrix = [
#     ["a", "b", "c"],
#     ["d", "e", "f"],
#     ["g", "h", "i"]
# ]
#
# # 每行内部用空格连接，行之间用换行连接
# result = "\n".join(" ".join(row) for row in matrix)
# print(result)
# # 输出:
# # a b c
# # d e f
# # g h i
# 2. 自定义格式化连接
# python
# # 连接时格式化元素
# values = [3.14159, 2.71828, 1.61803]
# formatted = " | ".join(f"{v:.3f}" for v in values)
# print(formatted)  # 输出: 3.142 | 2.718 | 1.618
# 3. 路径拼接（替代 os.path.join）
# python
# # 构建文件路径
# folders = ["home", "user", "documents"]
# filename = "report.txt"
#
# # 类Unix系统
# path = "/".join(folders) + "/" + filename
# print(path)  # 输出: home/user/documents/report.txt
#
# # Windows系统
# windows_path = "\\".join(folders) + "\\" + filename
# print(windows_path)  # 输出: home\user\documents\report.txt

# Python 中的 format() 方法详解
# format() 是 Python 字符串格式化的核心方法，提供强大而灵活的字符串格式化功能。它在 Python 2.6+ 和 3.x 中均可用，是旧式 % 格式化的现代替代方案。
#
# 基本语法
# python
# formatted_string = "文本 {placeholder} 文本".format(value)
# {placeholder}：格式化字段，会被 format() 的参数替换
#
# 支持位置参数、关键字参数和复杂表达式
#
# 核心功能
# 1. 基本替换
# python
# # 位置参数
# print("{} 的年龄是 {}".format("Alice", 30))
# # Alice 的年龄是 30
#
# # 索引参数（可重复使用）
# print("{0} 喜欢 {1}，{0} 也喜欢 {2}".format("Bob", "Python", "Java"))
# # Bob 喜欢 Python，Bob 也喜欢 Java
#
# # 关键字参数
# print("名称: {name}, 价格: {price}".format(name="苹果", price=5.5))
# # 名称: 苹果, 价格: 5.5
# 2. 混合使用
# python
# # 位置参数和关键字参数混合
# print("{1} 的 {item} 售价 ${price:.2f}".format(
#     "商店",
#     item="笔记本",
#     price=12.99,
#     name="Alice"
# ))
# # 笔记本 的 笔记本 售价 $12.99
# 3. 容器访问
# python
# # 列表访问
# data = ["Python", 3.9]
# print("语言: {0[0]}, 版本: {0[1]}".format(data))
# # 语言: Python, 版本: 3.9
#
# # 字典访问
# person = {"name": "Charlie", "age": 28}
# print("姓名: {p[name]}, 年龄: {p[age]}".format(p=person))
# # 姓名: Charlie, 年龄: 28
# 高级格式化选项
# 1. 对齐与填充
# 语法：{:[填充字符][对齐方式][宽度]}
#
# 对齐方式	符号	示例	结果
# 左对齐	<	"{:<10}".format("Hi")	Hi
# 右对齐	>	"{:>10}".format("Hi")	Hi
# 居中对齐	^	"{:^10}".format("Hi")	Hi
# 填充字符		"{:*^10}".format("Hi")	****Hi****
# 2. 数字格式化
# python
# # 整数格式
# print("{:d}".format(42))        # 42 (十进制)
# print("{:b}".format(42))        # 101010 (二进制)
# print("{:o}".format(42))        # 52 (八进制)
# print("{:x}".format(42))        # 2a (十六进制小写)
# print("{:X}".format(42))        # 2A (十六进制大写)
#
# # 浮点数格式
# print("{:.2f}".format(3.14159)) # 3.14 (保留2位小数)
# print("{:+.2f}".format(3.14))   # +3.14 (显示符号)
# print("{:.0f}".format(3.6))     # 4 (四舍五入取整)
#
# # 千位分隔符
# print("{:,}".format(1000000))   # 1,000,000
# 3. 类型转换
# python
# print("{!s}".format(123))      # '123' (str()转换)
# print("{!r}".format("text"))   # "'text'" (repr()转换)
# print("{!a}".format("中文"))   # "'\\u4e2d\\u6587'" (ASCII转换)
# 4. 日期时间格式化
# python
# from datetime import datetime
# now = datetime.now()
#
# print("{:%Y-%m-%d %H:%M:%S}".format(now))
# # 2023-08-05 14:30:45
#
# print("{:%A, %B %d, %Y}".format(now))
# # Saturday, August 05, 2023
# 高级用法
# 1. 动态格式
# python
# # 动态设置宽度和精度
# width = 10
# precision = 3
# value = 3.14159
#
# print("{:{width}.{precision}f}".format(
#     value,
#     width=width,
#     precision=precision
# ))
# #      3.142
# 2. 嵌套字段
# python
# # 字段内的字段
# print("{:{align}{width}}".format(
#     "text",
#     align='^',
#     width=10
# ))
# #   text    (居中对齐，宽度10)
# 3. 格式化类实例
# python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __format__(self, format_spec):
#         if format_spec == "short":
#             return self.name[0]
#         elif format_spec == "long":
#             return f"{self.name} ({self.age})"
#         return self.name
#
# p = Person("David", 40)
# print("{:short}".format(p))  # D
# print("{:long}".format(p))   # David (40)
# 4. 复杂数据结构
# python
# # 列表推导式与格式结合
# numbers = [1234, 56.789, -7]
# formatted = [f"{n:>10,.2f}" for n in numbers]
# print("\n".join(formatted))
# # 输出:
# #   1,234.00
# #      56.79
# #      -7.00