# for
# 打印0到9的数字
for i in range(10):
    print(i)

# 打印1到5的数字，步长为1（默认）
for i in range(1, 6):
    print(i)

# 打印2到10的偶数
for i in range(2, 11, 2):
    print(i)

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串中的每个字符
word = "hello"
for char in word:
    print(char)

# 遍历字典的键
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in my_dict:
    print(key)

# 同时遍历字典的键和值
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 打印0到9的数字，但遇到5时退出循环
for i in range(10):
    if i == 5:
        break  # 当i等于5时，退出循环
    print(i)

    # 输出: 0 1 2 3 4

# 当条件变量小于5时，循环继续；遇到特定条件时退出
count = 0
while True:
    count += 1
    if count > 5:
        break  # 当count大于5时，退出循环
    print(count)

    # 输出: 1 2 3 4 5

# 打印0到9的数字，但跳过偶数
for i in range(10):
    if i % 2 == 0:
        continue  # 如果i是偶数，跳过当前循环的剩余部分
    print(i)

    # 输出: 1 3 5 7 9

# 当条件变量小于10时，循环继续；但跳过特定值的迭代
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # 如果count是偶数，跳过当前循环的剩余部分
    print(count)

    # 输出: 1 3 5 7 9


# 定义一个空的函数
def my_function():
    pass


# 在条件语句中什么都不做
if True:
    pass  # 这里的pass表示不执行任何操作

# 在循环中占位，虽然这个循环实际上什么也不做
for i in range(5):
    pass  # 占位，不执行任何操作