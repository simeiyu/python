'''
8.6 将函数存储在模块中
---------------------
导入模块的方法有多种
'''

'''
8.6.1 导入整个模块
-----
要让函数是可导入的，得先创建模块。
模块是扩展名为.py的文件，包含要导入到程序中的代码。

例子，在modules/pizza.py，import在modules/making_pizzas.py
'''

'''
8.6.2 导入特定的函数
-----
语法：from module_name import function_name
通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
from module_name import function_0, function_1, function_2
'''

'''
8.6.3 使用as给函数指定别名
-----
语法：from module_name import function_name as new_name
'''

'''
8.6.4 使用as给模块指定别名
-----
语法：import module_name as new_name
'''

'''
8.6.5 导入模块中的所有函数
-----
语法：from module_name import *
'''