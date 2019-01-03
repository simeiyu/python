'''
7.3 使用while循环来处理列表和字典
-------------------------------
for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪
其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。
通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。
-------------------------------

7.3.1 在列表之间移动元素
'''
# 首先，创建一个待验证用户列表
#  和一个用于存储已验证用户的空列表
unconfirmed_user = ['alice', 'brian', 'candace']
confirmed_user = []

# 验证每个用户，直到没有未验证用户为止
#  将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print("Verifying user: " + current_user.title())
    confirmed_user.append(current_user)

# 显示所有已验证的用户
for user in confirmed_user:
    print(user.title())

'''
7.3.2 删除包含特定值的所有列表元素
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print('pets -->' + str(pets))
while 'cat' in pets:
    pets.remove('cat')

print('after remove cat -->', str(pets))

'''
7.3.3 使用用户输入来填充字典
'''
responses = {}
polling_active = True
while polling_active:
    name = input('What is your name?')
    response = input('Which mountain would you like to climb someday?')
    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/ no)')
    if repeat == 'no':
        polling_active = False
print('\n---- Poll Results ----')
for name, response in responses.items():
    print(name +' would like to climb ' + response + '.')

'''
动手试一试
'''
# 熟食店
sandwich_orders = ['one egg', 'miles', 'fruits', 'shucai']
finished_sandwiches = []
while sandwich_orders:
    sandwich_removed = sandwich_orders.pop(0)
    print('I made your ' + sandwich_removed + ' sandwich.')
    finished_sandwiches.append(sandwich_removed)

print(sandwich_orders)
print(finished_sandwiches)

# 梦想的度假胜地
resorts = {}
asking = True
while asking:
    name = input('What is your name?')
    question = input('If you could visit one place in the world, where would you go?')
    resorts[name] = question
    go_on = input('Would you like to let another person respond? (yes/ no)')
    if go_on == 'no':
        asking = False

for name, resort in resorts:
    print(name + ' would like to go ' + resort + '.')
    