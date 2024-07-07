# 算术运算符示例
result = 10 + 5 * 2  # 注意乘法优先于加法
print(result)  # 输出: 20

# 使用括号改变优先级
result = (10 + 5) * 2
print(result)  # 输出: 30

# 幂运算
result = 2 ** 3
print(result)  # 输出: 8

# 整除和取模
result = 10 // 3  # 整除
print(result)  # 输出: 3

result = 10 % 3  # 取模
print(result)  # 输出: 1

# 比较运算符示例
a = 5
b = 3

result = a > b
print(result)  # 输出: True

result = a <= b
print(result)  # 输出: False

# 逻辑运算符示例
result = True and False
print(result)  # 输出: False

result = True or False
print(result)  # 输出: True

result = not True
print(result)  # 输出: False

# 赋值运算符示例
a = 5
a += 3  # 相当于 a = a + 3
print(a)  # 输出: 8

a *= 2  # 相当于 a = a * 2
print(a)  # 输出: 16

# 运算符优先级示例
result = 2 + 3 * 2 ** 2  # ** 的优先级高于 *，而 * 的优先级高于 +
print(result)  # 输出: 14 (因为 2 ** 2 = 4, 3 * 4 = 12, 2 + 12 = 14)

# 使用括号改变优先级
result = (2 + 3) * (2 ** 2)
print(result)  # 输出: 20 (因为 2 + 3 = 5, 2 ** 2 = 4, 5 * 4 = 20)