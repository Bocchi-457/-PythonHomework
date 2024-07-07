# tuple
# 定义一个元组 t
t = (1,2,3,4,5,'a','b','c','d','e')
print(t)
# 打印元组的第一个元素
print(t[0])
# 打印元组的第二个到第三个元素（不包含第三个元素）
print(t[1:3])
# 计算元组中数字 3 出现的次数
print(t.count(3))
# 查找元组中字符串 'a' 的索引位置
print(t.index('a'))
# 逆序打印元组中的元素
print(t[::-1])

# tuple unpacking
# 定义一个元组 t1
t1 = (1,2,3)
# 解包元组 t1，将元素分别赋值给变量 a, b, c
a,b,c = t1
print(a,b,c)