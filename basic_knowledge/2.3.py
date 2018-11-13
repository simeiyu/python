'''
2.3 字符串
-----
在Python中，用引号括起来的都是字符串，可以是单引号，也可以是双引号。
'''

"""
2.3.1 修改字符串的大小写
"""
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

"""
2.3.2 合并拼接字符串
Python中使用加号（+）来拼接字符串
"""
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print('Hello, ' + full_name.title() + '!')

# 将消息存储在变量中
message = 'Hello, ' + full_name.title() + '!'
print(message)

"""
2.3.3 使用制表符或换行符来添加空白
      要在字符串中添加制表符，可使用字符组合\t，添加换行符，可使用\n。
"""
message = '\tPython,\n\tOpen a new world!'
print(message)

"""
2.3.4 删除空白
"""
favorite_language = '  Python   '
print(favorite_language.lstrip()) # 剔除开头空白
print(favorite_language.rstrip()) # 剔除结尾空白
print(favorite_language.strip())  # 剔除两端空白


