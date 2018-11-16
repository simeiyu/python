'''
第6章 字典
'''
# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

'''
6.2 使用字典
-----------
在Python中，字典是一系列键值对，
每个键都有一个值相关联，可以使用键来访问与之相关联的值。
与键相关联的值可以是数字、字符串、列表乃至字典，可以将任何Python对象用作字典中的值。
'''
# 访问字典中的值
# 指定字典名和放在方括号内的键，如下：
alien_0['color']

# 添加键值对
# 字典是动态结构，可随时在其中添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 先创建一个空字典
# 使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典
alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 8
print(alien_1)

# 修改字典中的值
alien_1["color"] = 'brown'
print("The alien_1 is now " + alien_1['color'])

print("Original x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print("New x-position: " + str(alien_0['x_position']))

# 删除键值对
del alien_0['points']  # 彻底删除了
print(alien_0)

# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
print(favorite_languages)
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    '.')

'''
动手练一练
'''
kids = [
    {
        'first_name': 'Lei',
        'last_name': 'Lee',
        'age': 12,
        'city': 'Beijing'
    }, {
        'first_name': 'Meimei',
        'last_name': 'Han',
        'age': 10,
        'city': 'Shanghai'
    }, {
        'first_name': 'Jim',
        'last_name': 'Green',
        'age': 14,
        'city': 'New York'
    }
]

if kids:
    for kid in kids:
        print('\nHello, my name is ' +
            kid['first_name'] + ' ' + kid['last_name'] +
            ', I am ' + str(kid['age']) + ' years old and come from ' +
            kid['city'] + '.')
    
    print("Welcome these " + str(len(kids)) + " new students.")
