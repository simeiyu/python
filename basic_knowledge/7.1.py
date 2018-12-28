'''
第7章 用户输入和while循环
-----------------------
通过获取用户输入并学会控制程序的运行时间，可编写出交互式程序。

7.1 函数input()的工作原理

函数input()让程序暂停运行，等待用户输入一些文本。
获取用户输入后，Python将其存储在一个变量中，以方便你使用。
使用input()时，Python将用户输入解读为字符串。
'''

message = input("Tell me something, and I'll repeat it back to you!")
print(message)

'''
7.1.1 编写清晰的程序

每当使用input()函数时，都应制定清晰而易于明白的提示。
如果提示超过一行，这时可将提示存储在一个变量中，再将该变量传递给函数input()。
'''
name = input("Please enter your name:")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("Hello, " + name + '!')

'''
7.1.2 使用int()来获取数值输入
'''
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are enough old!")
else:
    print("You are too young!")

'''
7.1.3 取模运算符 %
它将两个数相除并返回余数。
'''
number = input("Please enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

