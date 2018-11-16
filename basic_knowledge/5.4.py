'''
5.4 使用if语句处理列表
'''
# 确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + '.')
    print("Finished making pizza!")
else:
    print("Are you sure you want a plain pizza.")

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                    'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print("Finished making your pizza.")


