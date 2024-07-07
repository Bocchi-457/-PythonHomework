#set

# 创建一个包含整数的集合
num = {10, 20, 30}
# 创建一个包含字符串的集合
alpha = set('abcde')
print(num)  # 打印集合 num
print(alpha)  # 打印集合 alpha

# 集合中的元素是唯一的，所以重复的元素会被忽略
s1 = {10, 20, 10, 30, 20}
print(s1)  # 打印集合 s1
print(s1 is num)  # 判断 s1 和 num 是否是同一个集合对象（地址相同）
print(s1 == num)  # 判断 s1 和 num 是否包含相同的元素
print(type({}))  # 打印空集合的类型

# 向集合中添加一个元素
s1.add(40)
print(s1)  # 打印更新后的集合 s1

# 使用列表更新集合（列表中重复的元素也会被忽略）
s1.update([2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9])
print(s1)  # 打印更新后的集合 s1

# 打印空元组的类型（这里其实与集合无关，但为了演示类型检查）
print(type(()))

# 从集合中删除一个元素（如果元素不存在会抛出 KeyError，但 remove 方法不会）
s1.remove(20)
# discard 方法也会从集合中删除一个元素，但如果元素不存在则不会抛出异常
s1.discard(15)

# pop 方法会随机删除并返回一个元素（如果集合为空会抛出 KeyError）
print(s1.pop())  # 打印被删除的元素

# 判断元素是否存在于集合中
print(1 in s1)  # 判断 1 是否在 s1 中
print(10 in s1)  # 判断 10 是否在 s1 中