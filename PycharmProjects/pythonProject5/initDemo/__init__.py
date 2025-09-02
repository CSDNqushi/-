#  1. （Package）
# 作用：将普通目录标记为 Python 包，使 Python 解释器能识别并导入包内的模块。
# 示例：在目录 my_package/下创建空文件 __init__.py，该目录即成为可导入的包。

# 2. 初始化包
# 作用：包被导入时，__init__.py的代码自动执行，常用于：
# 设置包级常量（如 VERSION = "1.0.0"）。
# 执行启动代码（如数据库连接、环境检查）。
# 加载配置文件或依赖项
# __init__.py
print("初始化包...")
DATABASE_CONFIG = {"host": "localhost"}