'''
5.3 if语句
'''
# 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")

# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are too young to vote!")

# if-elif-else结构
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# 省略else代码块
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

# 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese':
    print("Adding extra cheese")
print("\nFinished making your pizza")
