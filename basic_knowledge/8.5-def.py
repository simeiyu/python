'''
8.5 传递任意数量的实参
---------------------
Python允许函数从调用语句中收集任意数量的实参。
形参名 *toppings 中的 * 让Python创建一个名为toppings的空元组，并将所有收到的值都封装到这个空元组中。即便函数只收到一个值。
'''
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(topping)
    # print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green_peppers', 'extra_cheese')

'''
8.5.1 结合使用位置实参和任意数量实参
-----
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
'''
def make_pizza2(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(topping)

make_pizza2(8, 'mushrooms', 'green_peppers', 'extra_cheese')

'''
8.5.2 使用任意数量的关键字实参
-----
形参 **user_info 中的两个星号让Python创建一个名为user_info的空字典，并将所有收到的名称-值对都封装到这个字典中。
在这个函数中，可以像访问其他字典一样访问user_info中的名称-值对
'''
def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Li', 'Lei', age=12, field='physician')
print(user_profile)
