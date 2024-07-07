# 定义布尔值
is_true = True
is_false = False

# 布尔运算
and_result = is_true and not is_false  # 结果为 True
or_result = is_false or is_true  # 结果为 True

print("AND Result:", and_result)
print("OR Result:", or_result)

# 布尔值在数值运算中的表现
result = is_true + 5  # 结果为 6，因为 True 等价于 1

print("Boolean in arithmetic:", result)