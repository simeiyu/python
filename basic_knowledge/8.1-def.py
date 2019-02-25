'''
第8章 函数
'''

'''
8.1 定义函数
'''
# 使用关键字def来告诉Python你要定义一个函数。
def greet_user(username):
    print('Hello ' + username)

greet_user('WangHao')

# 向函数传递信息

# 形参和实参
# 在函数greet_user的定义中，username是形参。
# 在代码 greet_user('WangHao')中，WangHao是一个实参。
# 实参是函数调用时传递给函数的信息。

'''
动手试一试
'''
# 消息
def display_message(msg):
    print('You said ' + '"' + msg + '" .')
message = input("您想说什么？")
display_message(message)

