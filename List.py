# 定义一个列表l
#list
l = [1,2,3,'a','b',[10,20]]
# 访问列表l中索引为5的元素（即子列表[10,20]），再访问该子列表中索引为0的元素（即10）
print(l[5][0])

# 定义一个名字列表name_list
name_list = ['Tom', 'Jerry', 'Louder', 'Judy']

# # 获取用户输入的名字，并进行搜索
# name = input('请输入你要搜索的名字：')
# if name in name_list:
#     print(f'你搜索的名字是{name}，名字已存在')
# else:
#     print(f'你搜索的名字是{name}，名字不存在')
#     name_list.append(name)

# 打印名字列表name_list
print(name_list)

# 向名字列表name_list中添加多个元素
name_list.extend(['Rupa','Subaru','Momoka','Tomo'])
print(name_list)

# 在名字列表name_list的索引为1的位置插入一个元素'kasumi'
name_list.insert(1,'kasumi')
print(name_list)

# 删除名字列表name_list中索引为1的元素
del name_list[1]

# 从名字列表name_list中删除元素'Rupa'
name_list.remove('Rupa')
print(name_list)

# 弹出名字列表name_list中的最后一个元素，并打印该元素
print(name_list.pop())

# 定义一个列表l，包含重复元素
l = [1,1,4,5,1,4]
# 对列表l进行排序
l.sort()
print(l)

# 反转列表l中的元素顺序
l.reverse()
print(l)

# 使用while循环遍历名字列表name_list，并打印每个元素
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# 使用for循环遍历名字列表name_list，并打印每个元素
for _ in name_list:
    print(_)

# 定义一个列表l0，包含两个元素，分别是列表l和名字列表name_list
l0=[l,name_list]
print(l0)

# 列表推导式
# 生成从20开始到98（不包含98），步长为2的整数列表
l = [i for i in range(20,100,2)]
print(l)

# 生成嵌套列表，外层列表的i从0到9，内层列表的j从10到19
l1 = [(i,j) for i in range(10) for j in range(10, 20)]
print(l1)


l1 = ['name', 'age', 'gender']
l2 = ['张三', 18, '男']
# 通过遍历l1和l2的索引i，将l1中的元素作为键，l2中的元素作为值，构建字典
d1 = {l1[i]:l2[i] for i in range(len(l1))}
print(d1)
# 使用zip函数将l1和l2打包成一个个元组，然后使用dict函数将这些元组转换成字典
d2 = dict(zip(l1, l2))
print(d2)

# 集合推导式
# 生成从0开始到8（不包含8），步长为2的整数集合
se = {i for i in range(0,10,2)}
print(se)