string_list = ["apple", "banana", "cherry"]
# 使用列表推导式和字符串切片+capitalize()
new_list = [s[0].capitalize() + s[1:] for s in string_list]

print(new_list)