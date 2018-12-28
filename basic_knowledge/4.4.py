'''
4.4 使用列表的一部分
------------------
处理列表的部分元素
'''
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:3]) # 从头开始
print(players[2:]) # 止于末尾
print(players[-3:]) # 从倒数第3个开始

# 遍历切片
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
copy_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend favorite foods are:")
print(friend_foods)
print("\nCopy favorite foods are:")
print(copy_foods)
