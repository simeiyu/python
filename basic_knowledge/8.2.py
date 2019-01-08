'''
8.2 传递实参
------------
调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
向函数传递参数的方式有很多，可使用位置实参、关键字实参、字典和列表。
'''
# 位置实参  最简单的关联方式：基于实参的顺序。位置实参的顺序很重要！
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'whillie')

# 关键字实参  是传递给函数的 名称-值 对。
# 直接在实参中将名称和值关联起来，向函数传递实参时不会混淆。
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 默认值  在编写函数时可以给每个形参指定默认值。
# 在函数调用中给形参提供了实参时，Python将使用指定的实参值；否则将使用形参的默认值。
def describe_pet2(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='Lucky')
describe_pet2(animal_type='hamster', pet_name='harry')

'''
试一试
'''
def mark_shirt(size, words):
    print('This shirt is ' + str(size) + ' and printed "' + words + '".')

mark_shirt(32, 'Hello world')
mark_shirt(size='L', words='I am a good baby!')

def describe_city(name, country='China'):
    print(name.title() + ' is in ' + country.title() + '.\n')
describe_city('shanghai')
describe_city(name='wuhan')
describe_city('Datian', 'Japanese')
