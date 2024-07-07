# module

import math

# 计算平方根
print(math.sqrt(16))  # 输出: 4.0

# 计算正弦值
print(math.sin(math.radians(30)))  # 输出接近 0.5，因为 30 度的正弦值是 0.5

# 计算自然对数的底 e
print(math.e)  # 输出: 2.718281828459045

from datetime import datetime, timedelta

# 获取当前日期和时间
now = datetime.now()
print("当前日期和时间:", now)

# 日期和时间运算
one_day_later = now + timedelta(days=1)
print("一天后的日期和时间:", one_day_later)

# 格式化日期和时间
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的日期和时间:", formatted_date)

import os

# 获取当前工作目录
print("当前工作目录:", os.getcwd())

# 列出目录内容
print("目录内容:", os.listdir('.'))

# 更改当前工作目录
os.chdir('/path/to/directory')  # 请替换为实际路径
print("更改后的工作目录:", os.getcwd())

# 创建新目录
os.mkdir('new_directory')

# 删除目录（请确保目录为空）
os.rmdir('new_directory')

import requests

# 发送 GET 请求
response = requests.get('https://api.github.com/users/github')

# 检查响应状态码
if response.status_code == 200:
    # 打印响应内容
    print(response.json())
else:
    print("请求失败，状态码:", response.status_code)

import json

# 将 Python 字典转换为 JSON 字符串
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}
json_str = json.dumps(data)
print("JSON 字符串:", json_str)

# 将 JSON 字符串解析为 Python 字典
json_data = json.loads(json_str)
print("解析后的 Python 字典:", json_data)