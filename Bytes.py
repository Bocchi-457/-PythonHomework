# 使用字节字面量创建bytes对象
bytes_obj1 = b'hello'  # 注意前面的b前缀

# 使用bytes()构造函数从字符串创建bytes对象，指定编码
bytes_obj2 = bytes('hello', encoding='utf-8')

# 使用bytes()构造函数从整数列表创建bytes对象
bytes_obj3 = bytes([72, 101, 108, 108, 111])  # 对应于'Hello'的ASCII码

print(bytes_obj1)  # 输出: b'hello'
print(bytes_obj2)  # 输出: b'hello'
print(bytes_obj3)  # 输出: b'Hello'

# 索引
print(bytes_obj3[0])  # 输出: 72

# 切片
print(bytes_obj3[1:4])  # 输出: b'ell'
# 错误示例：尝试修改bytes对象（会引发TypeError）
# bytes_obj3[0] = 65  # 'A'的ASCII码

# 正确做法：创建新的bytes对象
new_bytes_obj = bytes_obj3[:1] + b'A' + bytes_obj3[2:]
print(new_bytes_obj)  # 输出: b'HAllo'

# bytes对象转字符串
str_from_bytes = bytes_obj1.decode('utf-8')
print(str_from_bytes)  # 输出: hello

# 字符串转bytes对象
bytes_from_str = str_from_bytes.encode('utf-8')
print(bytes_from_str)  # 输出: b'hello'

# 遍历bytes对象中的每个字节
for byte in bytes_obj3:
    print(byte)  # 输出每个字节的整数值


# 假设的“加密”函数（简单地将每个字节增加1）
def simple_encrypt(data):
    return bytes([b + 1 for b in data])


# 加密
encrypted_data = simple_encrypt(bytes_obj3)
print(encrypted_data)  # 输出: b'IFmmp' 或类似的，取决于原始数据

# 注意：这里没有提供解密函数，因为简单的“加密”可能会导致字节超出范围（例如，'z'变成'{'）
# 在实际应用中，加密应该使用专业的库，如PyCryptoDome或cryptography。