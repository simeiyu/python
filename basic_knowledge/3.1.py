'''
第3章 列表简介
-------------
3.1 列表是什么
在Python中，用方括号（[]）来表示列表，并用逗号来分割其中的元素。
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""
3.1.1 访问列表元素
"""
print(bicycles[0])

# 通过将索引指定为 -1，可以让Python返回最后一个列表元素。
# -2 返回倒数第二个列表元素，-3 返回倒数第三个，以此类推。
print(bicycles[-1])

"""
3.2 修改、添加、删除元素
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

# 在列表中插入元素
motorcycles.insert(0, 'qianjiang')  # 新元素的索引和值
print(motorcycles)

# 从列表中删除元素
del motorcycles[-1]
print(motorcycles)

# 使用方法pop()删除末尾的元素
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

# 使用方法pop()删除列表任何位置的元素
# 只需在括号中指定要删除的元素的索引
second_owned = motorcycles.pop(1)
print(second_owned)
print(motorcycles)

motorcycles.append('honda')

# 根据值删除元素
motorcycles.remove('qianjiang')
print(motorcycles)
