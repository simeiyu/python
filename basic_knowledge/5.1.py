'''
第5章 if语句
'''
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 在Python中检查是否相等时区分大小写
print('Audi' != 'audi')

# 检查多个条件
age = 24
print(age >= 20 and age <= 40)
print(age >= 30 and age <= 40)
print(age >= 30 or age <= 40)

# 检查特定值是否包含在列表中
print('subaru' in cars)
print('zontai' in cars)
print('subaru' not in cars)

# 布尔表达式
# 布尔表达式通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站内容。
game_active = True
can_edit = False
