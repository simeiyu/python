'''
4.3 创建数值列表
Python提供了很多工具，帮助高效的处理数字列表
'''
# 使用函数range()
for value in range(1, 5):
    print(value)

result_range = range(0, 6)
print(result_range)

# 使用range()创建数字列表
# 可以使用list()将range()的结果直接转换为列表
result_list = list(result_range)
print(result_list)

# 使用range()还可以指定步长
for even in range(2, 11, 2):
    print(even)

# 前10个整数的平方组成的列表
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# 对数字列表执行简单的统计运算
print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares = [value ** 2 for value in range(1, 11)]
print('列表解析：' + str(squares))


inputData = [{
  "code": 0,
  "data": {
    "result": [["1", "2", "3"]],
    "pageSize": 20,
    "pageCount": 12,
    "currentPage": 11,
    "total": 123
  }
}, {
  "code": 0,
  "data": {
    "result": [["a", "b", "c"]],
    "pageSize": 10,
    "pageCount": 2,
    "currentPage": 1,
    "total": 123
  }
}]
{f"out{k[-1]}": {"pageSize": v["data"]["pageSize"], "pageCount": v["data"]["pageCount"], "currentPage": v["data"]["currentPage"]} for k, v in locals().items() if k.startswith("inputData") and v}

'''
动手试一试
'''
# 1~20的奇数
print(list(range(1, 21, 2)))

# 3~30内能被3整除的数字列表
print(list(range(3, 31, 3)))

# 1~10的立方值列表
print([value ** 3 for value in range(1, 11)])
