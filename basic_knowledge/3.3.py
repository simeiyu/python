'''
3.3 组织列表

3.3.1 使用方法sort()对列表进行永久性排序
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 按与字母顺序相反的顺序排序
cars.sort(reverse=True)
print(cars)

'''
3.3.2 使用方法sorted()对列表进行临时性排序
也可以向sorted()传递参数reverse=True
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)

print("Here is the sorted list: ")
print(sorted(cars))

print("Here is the original list again: ")
print(cars)

'''
3.3.3 倒着打印列表
'''
# reverse()永久性的反转列表元素的排列顺序
cars.reverse()
print(cars)

'''
3.3.4 确定列表的长度
'''
# 使用len()可快速获悉列表的长度
len(cars)
