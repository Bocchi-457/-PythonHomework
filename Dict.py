# 定义一个字典 d
dict
d = {'name': 'Tom', 'age': 18, 'gender': 'male'}
# 打印字典 d 中键为 'name' 的值
print(d['name'])
# 使用 get 方法打印字典 d 中键为 'age' 的值
print(d.get('age'))
# 打印整个字典 d
print(d)
# 打印字典 d 的键值对（以元组形式）
print(d.items())
# 遍历字典 d 的键，并打印每个键
for _ in d:
    print(_)
# 遍历字典 d 的值，并打印每个值
for _ in d.values():
    print(_)
# 遍历字典 d 的键，并打印每个键
for _ in d.keys():
    print(_)
# 遍历字典 d 的键值对，并打印每个键值对的键和值
for key, value in d.items():
    print(f'{key}={value}')

