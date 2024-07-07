# string

# 查找子字符串"Python"在字符串s中的位置
#string
s = 'Hello,Python!I love Python programming.'
Index = s.find('Python')
if Index != -1:
    # 如果找到"Python"，则打印其位置，并替换为"Java"后打印新字符串
    print(f'"Python"在字符串中的位置是：{Index}')
    print(s.replace('Python', 'Java'))
else:
    # 如果没有找到"Python"，则打印提示信息
    print('"Python"不在字符串中')


# 去除字符串s两侧的空白字符
s = '        Hello      '
print(s.lstrip())  # 去除左侧空白字符
print(s.rstrip())  # 去除右侧空白字符
print(s.strip())   # 去除两侧空白字符

# 字符串s的对齐操作
print(s.ljust(30, '.'))  # 左对齐，并用'.'填充至总长度为30
print(s.rjust(30, '*'))  # 右对齐，并用'*'填充至总长度为30
print(s.center(30, '-')) # 居中对齐，并用'-'填充至总长度为30


# 字符串s的开头和结尾判断
s = 'Man!What can I say!'
print(s.startswith('Man'))      # 判断是否以"Man"开头
print(s.startswith('can', 9,12)) # 判断从索引9到12的子串是否以"can"开头
print(s.endswith('!'))         # 判断是否以"!"结尾
print(s.endswith('ay!',10, 17)) # 判断从索引10到17的子串是否以"ay!"结尾
print(s.endswith('a',10, 17))   # 判断从索引10到17的子串是否以"a"结尾
print(s[16])                   # 打印索引为16的字符


# 字符串s1, s2, s3的字符类型判断
s1 = 'Man114514'
s2 = '114514'
s3 = 'Man'
print(s1.isdigit())       # 判断s1是否全部由数字组成
print(s2.isdigit())       # 判断s2是否全部由数字组成
print(s3.isdigit())       # 判断s3是否全部由数字组成
print(s1.isalpha())       # 判断s1是否全部由字母组成
print(s2.isalpha())       # 判断s2是否全部由字母组成
print(s3.isalpha())       # 判断s3是否全部由字母组成
print(s1.isalnum())       # 判断s1是否全部由字母或数字组成
print(s2.isalnum())       # 判断s2是否全部由字母或数字组成
print(s3.isalnum())       # 判断s3是否全部由字母或数字组成
print(s1.isspace())       # 判断s1是否全部由空白字符组成