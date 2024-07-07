# while
i = 0
while i < 5:
    # 打印 "我中了"
    print('我中了')
    # i自增1
    i += 1

# 第二个循环块
i = 1
result = 0
while i <= 100:
    # result累加i
    result += i
    # i自增1
    i += 1
# 打印result
print(result)

# 第三个循环块
i = 1
while i <= 5:
    # 如果i等于4
    if i == 4:
        # 打印 "吃饱了，不吃了"
        print("吃饱了，不吃了")
        # 跳出循环
        break
    # 打印 "吃了第i个苹果"
    print(f'吃了第{i}个苹果')
    # i自增1
    i += 1

# 第四个循环块
j = 0
while j <= 4:
    i = 0
    while i <= 4:
        # 打印 "*"
        print("*", end='')
        # i自增1
        i += 1
    # 换行
    print()
    # j自增1
    j += 1

# 第五个循环块
j = 0
while j <= 19:
    i = 0
    # 注释掉的内嵌循环块
    # while i <= j:
    #     print("*", end='')
    #     i += 1
    # 打印由j个"*"组成的字符串，并居中显示在21个字符宽度的字符串中
    print(("*" * j).center(21))
    # j自增1
    j += 1

# 第六个循环块
i = 1
while i < 10:
    j = 1
    while j <= i:
        # 打印乘法表达式
        print(f'{j}x{i}={i*j}', end=' ')
        # j自增1
        j += 1
    # 换行
    print()
    # i自增1
    i += 1