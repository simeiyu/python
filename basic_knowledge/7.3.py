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