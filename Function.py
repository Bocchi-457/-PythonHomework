# function
def sum(a,b):
    # 打印两个数字的和
    print(a+b)
    # 返回两个数字的和
    return a+b

# 输入两个数字
a,b = (input("请输入两个数字：")).split(' ')
# 调用sum函数计算并打印两个数字的和
sum(int(a), int(b))

def sum_num(a,b,c):
    # 返回三个数字的和
    return a+b+c

def average(a,b,c):
    # 调用sum_num函数计算三个数字的和，然后除以3得到平均值
    return sum_num(a,b,c)/3

# 输入三个数字
a,b,c = (input("请输入三个数字：")).split(' ')
# 调用sum_num函数计算并打印三个数字的和
print(sum_num(int(a), int(b), int(c)))
# 调用average函数计算并打印三个数字的平均值
print(average(int(a), int(b), int(c)))


def user_info(name, age, gender):
    # 打印用户信息
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

# 调用user_info函数并传入参数
user_info('张三', 18, '男')

def test(d):
    # 创建一个新的字典，其中原字典的键作为值，原字典的值作为键
    tmp = {v: k for k, v in d.items()}
    return tmp

# 创建一个字典
d = {'a':1, 'b':2, 'c':3}
# 调用test函数并传入字典d，然后将结果重新赋值给d
d = test(d)
# 打印字典d
print(d)

# 递归

def yeshu(n):
    # 如果n大于6，则返回0
    if n > 6:
        return 0
    # 如果n等于6，则返回3
    elif n == 6:
        return 3
    else:
        # 递归调用yeshu函数，并将n+1作为参数传入，然后将结果乘以2再加2
        return (yeshu(n+1)+2)*2

# 调用yeshu函数并传入参数1，然后打印结果
print(yeshu(1))

#abs()
a = -1
# 打印a的绝对值
print(abs(a))


#map()
l1 = [1, 2, 3, 4, 5]
# 调用map函数，使用lambda函数将列表l1中的每个元素加1，并将结果赋值给l2
l2  = map(lambda x:x+1, l1)
# 将map对象转换为列表并打印
print(list(l2))


#reduce()
from functools import reduce
l1 = [1, 2, 3, 4, 5]
# 调用reduce函数，使用lambda函数将列表l1中的元素累加，并将结果赋值给result
result = reduce(lambda x, y:x+y, l1)
# 打印累加结果
print(result)

# 定义一个简单的lambda函数，计算两个数的和
add = lambda x, y: x + y

# 调用lambda函数
result = add(5, 3)
print(result)  # 输出: 8

# 使用lambda函数过滤出列表中的偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = filter(lambda x: x % 2 == 0, numbers)

# 将filter对象转换为列表
print(list(filtered))  # 输出: [2, 4, 6, 8, 10]

# 使用lambda函数将列表中的每个元素乘以2
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)

# 将map对象转换为列表
print(list(squared))  # 输出: [1, 4, 9, 16, 25]

# 使用lambda函数对元组的列表进行排序，基于元组的第二个元素
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs_sorted = sorted(pairs, key=lambda pair: pair[1])

print(pairs_sorted)  # 输出: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# 也可以逆序排序
pairs_sorted_desc = sorted(pairs, key=lambda pair: pair[1], reverse=True)
print(pairs_sorted_desc)  # 输出: [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]

# 示例：不太常见的用法，仅作为展示
numbers = [1, 2, 3, 4, 5]
squared = [lambda x: x * x for _ in numbers]  # 注意：这里创建了一个lambda函数的列表，而不是它们的调用结果

# 如果你想调用它们，需要这样做（但通常不推荐这样做）
print([f(2) for f in squared])  # 输出: [4, 4, 4, 4, 4]，因为每个lambda都计算2的平方

# 更常见的做法是直接在列表推导式中计算值
squared_values = [x * x for x in numbers]
print(squared_values)  # 输出: [1, 4, 9, 16, 25]