'''
4.5 元组
--------
Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
'''
# 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

'''
虽然不能修改元组，但是可以给存储元组的变量赋值。
'''
dimensions = (200, 120)
for dimension in dimensions:
    print(dimension)

'''
相比于列表，元组是更简单的数据结构。
如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。
'''

'''
动手试一试
'''
# 菜单
foods = ('地锅鸡', '木须肉', '麻辣鱼', '手撕鸡', '上汤娃娃菜')
print(foods)

# 新菜单
foods = ('口水鸡', '银鱼羹', '麻辣鱼', '手撕鸡', '锅包肉')
for food in foods:
    print(food) 
