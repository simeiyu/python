'''
2.4 数字

2.4.1 整数
在python中可对整数执行 + - * / 运算
python使用两个**表示乘方运算
python还支持运算次序
'''
print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 ** 3)

"""
2.4.2 浮点数
python中，带小数点的数字都是浮点数。
需要注意：小数的运算结果包含的小数位数可能是不确定的。
"""
print(0.2 + 0.3)
print(3 * 0.1)

"""
2.4.3 使用函数str()避免类型错误
"""
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)
