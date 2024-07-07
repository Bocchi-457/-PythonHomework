# 整数转浮点数
int_value = 10
float_value = float(int_value)
print(float_value)  # 输出: 10.0

# 浮点数转整数（注意：这会舍弃小数部分）
float_value = 10.5
int_value = int(float_value)
print(int_value)  # 输出: 10

# 字符串转整数
str_value = "123"
int_value = int(str_value)
print(int_value)  # 输出: 123

# 注意：字符串必须能够表示一个整数，否则会引发ValueError
# str_value = "abc"
# int_value = int(str_value)  # 这会抛出ValueError

# 整数转字符串
int_value = 123
str_value = str(int_value)
print(str_value)  # 输出: '123'

# 字符串转浮点数
str_value = "123.456"
float_value = float(str_value)
print(float_value)  # 输出: 123.456

# 注意：字符串必须能够表示一个浮点数，否则会引发ValueError
# str_value = "abc.def"
# float_value = float(str_value)  # 这会抛出ValueError

# 浮点数转字符串
float_value = 123.456
str_value = str(float_value)
print(str_value)  # 输出: '123.456'

# 数字0、空字符串、空列表等被视为False
zero = 0
empty_str = ""
empty_list = []

print(bool(zero))  # 输出: False
print(bool(empty_str))  # 输出: False
print(bool(empty_list))  # 输出: False

# 非零数字、非空字符串、非空列表等被视为True
non_zero = 1
non_empty_str = "hello"
non_empty_list = [1, 2, 3]

print(bool(non_zero))  # 输出: True
print(bool(non_empty_str))  # 输出: True
print(bool(non_empty_list))  # 输出: True

# 列表转元组
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print(tuple_value)  # 输出: (1, 2, 3)

# 元组转列表
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
print(list_value)  # 输出: [1, 2, 3]