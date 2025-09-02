# 在 Python 中，re 模块提供了正则表达式操作功能，用于字符串的匹配、搜索、替换和分割等操作。以下是核心函数和使用示例：
#
# 常用函数
# re.match(pattern, string)
# 从字符串开头匹配模式，返回匹配对象或 None。
#
# python
# import re
# result = re.match(r'hello', 'hello world')
# print(result.group())  # 输出: 'hello'
# re.search(pattern, string)
# 扫描整个字符串，返回第一个匹配对象或 None。
#
# python
# result = re.search(r'\d+', 'price: 100')
# print(result.group())  # 输出: '100'
# re.findall(pattern, string)
# 返回所有匹配的字符串列表。
#
# python
# results = re.findall(r'\d+', '1 apple, 2 oranges, 3 bananas')
# print(results)  # 输出: ['1', '2', '3']
# re.finditer(pattern, string)
# 返回匹配对象的迭代器（适合大文本）。
#
# python
# matches = re.finditer(r'\d+', '1, 2, 3')
# for match in matches:
#     print(match.group())  # 依次输出: '1', '2', '3'
# re.sub(pattern, repl, string)
# 替换匹配的子串，repl 可以是字符串或函数。
#
# python
# text = re.sub(r'\d+', 'X', 'a1b2c3')
# print(text)  # 输出: 'aXbXcX'
# re.split(pattern, string)
# 按模式分割字符串。
#
# python
# parts = re.split(r'\W+', 'apple, banana; cherry')
# print(parts)  # 输出: ['apple', 'banana', 'cherry']
# re.compile(pattern)
# 预编译正则表达式，提高重复使用效率。
#
# python
# pattern = re.compile(r'\d{3}-\d{4}')
# result = pattern.search('Tel: 123-4567')
# print(result.group())  # 输出: '123-4567'
# 匹配对象方法
# 匹配成功后返回的对象包含以下方法：
#
# .group()：返回匹配的完整字符串。
#
# .group(n)：返回第 n 个分组（() 捕获的内容）。
#
# .start() / .end()：匹配的起止位置。
#
# .span()：匹配的 (start, end) 元组。
#
# 示例：
#
# python
# match = re.search(r'(\d{3})-(\d{4})', 'Tel: 123-4567')
# print(match.group())    # '123-4567'
# print(match.group(1))   # '123'
# print(match.group(2))   # '4567'
# print(match.span())     # (5, 13)
# 正则表达式语法
# .：匹配任意字符（除换行符）。
#
# \d：数字（等价于 [0-9]）。
#
# \w：字母、数字、下划线。
#
# \s：空白字符（空格、制表符等）。
#
# *：0 次或多次重复。
#
# +：1 次或多次重复。
#
# ?：0 次或 1 次重复。
#
# {n}：精确匹配 n 次。
#
# [...]：字符集合（如 [a-z]）。
#
# ^ / $：字符串开始/结束。
#
# |：或逻辑（如 a|b）。
#
# ()：捕获分组。
#
# 高级技巧
# 非贪婪匹配：在量词后加 ?（如 .*?）。
#
# python
# re.findall(r'<.*?>', '<a> <b>')  # 输出: ['<a>', '<b>']（贪婪模式会匹配整个字符串）
# 分组命名：(?P<name>...)
#
# python
# match = re.search(r'(?P<area>\d{3})-(?P<num>\d{4})', '123-4567')
# print(match.group('area'))  # '123'
# 忽略大小写：re.IGNORECASE 标志。
#
# python
# re.search(r'hello', 'HELLO', re.IGNORECASE).group()  # 'HELLO'
# 多行模式：re.MULTILINE（使 ^/$ 匹配每行开头/结尾）。
#
# python
# re.findall(r'^\d+', '1\n2\n3', re.MULTILINE)  # ['1', '2', '3']
# 常见场景示例
# 验证邮箱格式：
#
# python
# email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
# if re.match(email_pattern, "user@example.com"):
#     print("Valid email")
# 提取 URL 中的域名：
#
# python
# url = "https://www.example.com/page"
# match = re.search(r'https?://([\w\.-]+)', url)
# print(match.group(1))  # 'www.example.com'
# 替换日期格式（YYYY-MM-DD → DD/MM/YYYY）：
#
# python
# text = "2023-10-05"
# result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
# print(result)  # "05/10/2023"
# 注意事项
# 特殊字符需转义（如 . → \.、* → \*）。
#
# 原始字符串建议用 r'...' 避免转义问题（如 r'\d'）。
#
# 复杂正则表达式可添加注释（re.VERBOSE 标志）。
#
# 通过灵活组合这些功能，re 模块能高效处理复杂的文本操作任务。