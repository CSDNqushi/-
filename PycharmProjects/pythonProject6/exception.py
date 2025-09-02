# 在 Python 中，else 子句、finally 子句和 raise 语句是异常处理和流程控制的重要组成部分。以下是它们的详细解释和用法：
#
# 1. else 子句（在异常处理中）
# 在 try-except 块中，else 子句用于定义当没有异常发生时要执行的代码。
#
# 语法：
# python
# try:
#     # 可能引发异常的代码
# except SomeException:
#     # 异常处理代码
# else:
#     # 没有异常时执行的代码
# finally:
#     # 无论是否异常都会执行的代码
# 特点：
# 仅在 try 块没有引发任何异常时执行
#
# 避免将主逻辑代码放在 try 块中（使代码更清晰）
#
# 在 except 之后、finally 之前
#
# 示例：
# python
# try:
#     result = 10 / int(input("输入除数: "))
# except ValueError:
#     print("请输入数字!")
# except ZeroDivisionError:
#     print("除数不能为零!")
# else:
#     print(f"计算结果: {result}")  # 仅当没有异常时执行
# 2. finally 子句
# 无论是否发生异常，finally 块中的代码总是会执行。常用于资源清理操作。
#
# 特点：
# 无论 try 块是否引发异常都会执行
#
# 即使有 return、break 或 continue 也会执行
#
# 在异常处理链中最后执行
#
# 常见用途：
# 关闭文件
#
# 释放网络连接
#
# 释放锁
#
# 清理资源
#
# 示例：
# python
# file = None
# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("文件不存在")
# finally:
#     if file:  # 确保文件对象存在
#         file.close()  # 无论是否异常都会关闭文件
#     print("资源清理完成")
# 3. raise 语句
# 用于主动引发异常，可以引发内置异常或自定义异常。
#
# 基本语法：
# python
# raise SomeException("错误描述")
# 主要用途：
# 主动触发异常
#
# 重新引发当前处理的异常
#
# 转换异常类型
#
# 在自定义异常中使用
#
# 使用示例：
# 情况1：引发内置异常
#
# python
# def validate_age(age):
#     if age < 0:
#         raise ValueError("年龄不能为负数")
#     if age < 18:
#         raise PermissionError("未成年人禁止访问")
#
# try:
#     validate_age(-5)
# except ValueError as e:
#     print(f"无效输入: {e}")
# 情况2：重新引发当前异常
#
# python
# try:
#     # 可能出错的代码
#     result = 10 / 0
# except ZeroDivisionError:
#     print("捕获到除零错误")
#     raise  # 重新引发相同的异常
# 情况3：转换异常类型
#
# python
# try:
#     # 可能出错的代码
#     with open("missing.txt") as f:
#         content = f.read()
# except FileNotFoundError as e:
#     raise RuntimeError("文件处理失败") from e
# 情况4：使用自定义异常
#
# python
# class InsufficientFundsError(Exception):
#     """自定义异常：余额不足"""
#     pass
#
# def withdraw(amount, balance):
#     if amount > balance:
#         raise InsufficientFundsError(f"余额不足! 当前余额: {balance}")
#     return balance - amount
#
# try:
#     withdraw(1000, 500)
# except InsufficientFundsError as e:
#     print(e)

# 在Python中，断言（assert）是一种调试工具，用于在代码中设置检查点，确保程序在某个条件为真时才能继续执行。如果条件为假，将触发AssertionError异常。
#  基本语法：
#      assert 条件表达式, 错误信息（可选）
#  当条件表达式为False时，抛出AssertionError，并显示可选错误信息；如果为True，则什么也不发生。
#  注意：断言通常用于开发阶段，帮助开发者快速定位问题。在生产环境中，可以通过运行Python时加上-O（大写字母O）选项来禁用断言（此时所有的assert语句将被忽略）。
#  示例：
#      assert 1 == 1   # 条件为真，通过
#      assert 1 == 2   # 条件为假，抛出AssertionError
#      带错误信息：
#         assert 1 == 2, "1不等于2"
#  使用场景：
#      1. 检查函数参数的合法性
#      2. 检查中间结果，确保程序逻辑正确
#      3. 检查程序执行的必要条件（如文件存在、变量类型等）
#  注意事项：
#      1. 不要用断言来检查用户输入，因为断言可以被全局禁用，导致检查失效。对于用户输入，应该使用if语句配合抛出异常（如ValueError）来处理。
#      2. 断言不应该用于处理程序逻辑中可预见的错误（如文件不存在、网络连接断开等），这些应该使用异常处理（try-except）。
#      3. 断言用于处理程序内部不应该发生的错误（即程序员的错误）。