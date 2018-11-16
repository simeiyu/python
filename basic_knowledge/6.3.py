'''
6.3 遍历字典
'''
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print(user_0.items())
print(user_0)

# 遍历所有的键值对
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 遍历所有的键
# print(user_0.keys())
for name in user_0.keys():
    print('\n' + name)

if 'tel' not in user_0.keys():
    print("Please pull your telephone")

# 按顺序遍历字典中的所有键
for name in sorted(user_0.keys()):
    print(name)

# 遍历字典中的所有值
for name in user_0.values():
    print(name)

print("\nSorted names: ")
for name in sorted(user_0.values()):
    print(name)
