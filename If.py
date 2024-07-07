# if elif else
age = int(input('请输入你的年龄：'))
# 如果年龄大于等于18
# if age >= 18:
#     print('成年人,请进')
# else:
#     print('未成年，请回家写作业')
# 如果年龄小于18
if age < 18:
    # 未成年，童工
    print('未成年，童工')
# 如果年龄在18到60之间（包括18，不包括60）
elif age <= 60:
    # 已成年，合法员工
    print('已成年，合法员工')
else:
    # 年龄已超过60，自愿返岗奉献
    print('年龄已超过60，自愿返岗奉献')

# random
import random
# 随机生成电脑出拳的数字（0-2）
computer = random.randint(0, 2)
# 玩家输入出拳的数字（0-石头，1-剪刀，2-布）
player = int(input('请出拳：0-石头，1-剪刀，2-布：'))
# 打印电脑出拳的结果
print(f'电脑出拳：{computer}')
# 判断玩家和电脑的出拳结果
if (player == 0 and computer == 1) or (player == 2 and computer == 0) or (player == 1 and computer == 2):
    # 如果玩家赢了
    print('你win了')
elif player == computer:
    # 如果平局
    print('平局')
else:
    # 如果玩家输了
    print('你输了')


# 三目运算符
a = 1
b = 2
# 如果a大于b，则c为a，否则c为b
c = a if a > b else b
# 打印c的值
print(c)