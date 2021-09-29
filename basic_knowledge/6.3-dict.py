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

in1 = [
    {
        "TASK_STATUS_CODE": "NEW",
        "TASK_STATUS_NAME": "新建",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "RELEASED",
        "TASK_STATUS_NAME": "已下达",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "RUNNING",
        "TASK_STATUS_NAME": "运行中",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "PENDING",
        "TASK_STATUS_NAME": "暂挂",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "PAUSE",
        "TASK_STATUS_NAME": "暂停",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "DISPATCHED",
        "TASK_STATUS_NAME": "已分派",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "QUEUING",
        "TASK_STATUS_NAME": "排队中",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "CANCELLED",
        "TASK_STATUS_NAME": "取消"
    },
    {
        "TASK_STATUS_CODE": "CLOSED",
        "TASK_STATUS_NAME": "关闭"
    },
    {
        "TASK_STATUS_CODE": "NEW",
        "TASK_STATUS_NAME": "新建",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "RELEASED",
        "TASK_STATUS_NAME": "已下达",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "RUNNING",
        "TASK_STATUS_NAME": "运行中",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "DISPATCHED",
        "TASK_STATUS_NAME": "已分派",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "QUEUING",
        "TASK_STATUS_NAME": "排队中",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "PENDING",
        "TASK_STATUS_NAME": "暂挂",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "PAUSE",
        "TASK_STATUS_NAME": "暂停",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "CANCELLED",
        "TASK_STATUS_NAME": "取消"
    },
    {
        "TASK_STATUS_CODE": "CLOSED",
        "TASK_STATUS_NAME": "关闭"
    },
    {
        "TASK_STATUS_CODE": "COMPLETED",
        "TASK_STATUS_NAME": "已完成"
    },
    {
        "TASK_STATUS_CODE": "EXCEPTION",
        "TASK_STATUS_NAME": "异常",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "SUSPENSED",
        "TASK_STATUS_NAME": "暂停下发",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "UNPACKING",
        "TASK_STATUS_NAME": "拆包中",
        "selected": True
    },
    {
        "TASK_STATUS_CODE": "UNPACKED",
        "TASK_STATUS_NAME": "拆包完成",
        "selected": True
    }
]

# [{"id": item["TASK_STATUS_CODE"], "text": item["TASK_STATUS_NAME"], "selected": item["selected"]} for item in in1]
out1 = []
for item in in1:
  selected = item["selected"]
  print(selected)
  out1.append({'id': item["TASK_STATUS_CODE"], 'text': item["TASK_STATUS_NAME"], 'selected': selected })
print(out1)