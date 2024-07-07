# random
import random

# 生成电脑出拳的数字（0-2）
computer = random.randint(0, 2)

# 获取玩家出拳的数字（0-石头，1-剪刀，2-布）
player = int(input('请出拳：0-石头，1-剪刀，2-布：'))

# 打印电脑出拳的结果
print(f'电脑出拳：{computer}')

# 判断胜负情况
if (player == 0 and computer == 1) or (player == 2 and computer == 0) or (player == 1 and computer == 2):
    # 玩家赢了
    print('你win了')
elif player == computer:
    # 平局
    print('平局')
else:
    # 玩家输了
    print('你输了')

