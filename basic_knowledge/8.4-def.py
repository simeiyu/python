'''
8.4 传递列表
------------
向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。
将列表传递给函数后，函数就能直接访问其内容。
下面使用函数来提高处理列表的效率。
'''
def greet_users(names):
    for name in names:
        print('Hello, ' + name.title() + '.')

usernames = ['Binbing', 'xun', 'huawei']
greet_users(usernames)

'''
8.4.1 在函数中修改列表
'''
# 将列表传递给函数后，函数就可以对其进行修改。
# 在函数中对这个列表所做的任何修改都是永久性的，这让你能够高效的处理大量数据。
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pandent', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 每个函数都应只负责一项具体的工作
# 编写函数时，如果发现他执行的任务太多，请尝试将这些代码划分到不同的函数中。
# 总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。

'''
8.4.1 禁止函数修改列表
'''
# 有时候，需要禁止函数修改列表。向函数传递列表的副本而不是原件，这样函数所做的任何修改都只影响副本而丝毫不影响原件。

unprinted_designs = ['iphone case', 'robot pandent', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(unprinted_designs)


