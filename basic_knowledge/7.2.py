'''
7.2 while循环简介
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != "quit":
        print(message)

'''
7.2.3 使用标志
在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。
这个变量被称为标志，充当了程序的交通信号灯。
'''
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

'''
7.2.4 使用break退出循环
'''
# 在用户输入'quit'后用break语句立即退出while循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 在任何Python循环中都可以使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。

'''
7.2.5 在循环中使用continue
要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句
'''
# 从1数到10，只打印其中奇数的循环
number = 0
while number < 10:
    number += 1

    if number % 2 == 0:
        continue
    else:
        print(number)

'''
7.2.6 避免无限循环
如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗口。
要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。
'''
