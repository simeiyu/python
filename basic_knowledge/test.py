# data = [
#   {
#     "erpMo": "AAA-1",
#     "erpBigSsCode": "AAA-2",
#     "erpBigSsName": "AAA-3",
#     "erpCurrentItem": "AAA-4",
#     "erpCurrentName": "AAA-5"
#   },
#   {
#     "erpMo": "BJ8-2103000908",
#     "erpBigSsCode": "11152901",
#     "erpBigSsName": "生产三部冲压一线",
#     "erpCurrentItem": "20810802817",
#     "erpCurrentName": "主机附面板（自动线）"
#   },
#   {
#     "erpMo": "BJ8-2103000923",
#     "erpBigSsCode": "11152901",
#     "erpBigSsName": "生产三部冲压一线",
#     "erpCurrentItem": "20833300703",
#     "erpCurrentName": "油杯（冲压）"
#   }
# ]

# [[k[i] for i,j in data[0].items() ] for k in data]

# 公式编辑器 -  [{},{},{}] 转 [[],[],[],[]]
# {f"out{k[-1]}": [[r[i] for i,j in v[0].items() ]for r in v] for k, v in locals().items() if k.startswith("inputData") and v}

# data = [{"TASK_STATUS_CODE":"NEW","TASK_STATUS_NAME":"新建"},{"TASK_STATUS_CODE":"RELEASED","TASK_STATUS_NAME":"已下达"},{"TASK_STATUS_CODE":"RUNNING","TASK_STATUS_NAME":"运行中"},{"TASK_STATUS_CODE":"PENDING","TASK_STATUS_NAME":"暂挂"},{"TASK_STATUS_CODE":"PAUSE","TASK_STATUS_NAME":"暂停"},{"TASK_STATUS_CODE":"DISPATCHED","TASK_STATUS_NAME":"已分派"},{"TASK_STATUS_CODE":"QUEUING","TASK_STATUS_NAME":"排队中"},{"TASK_STATUS_CODE":"CANCELLED","TASK_STATUS_NAME":"取消"},{"TASK_STATUS_CODE":"CLOSED","TASK_STATUS_NAME":"关闭"},{"TASK_STATUS_CODE":"NEW","TASK_STATUS_NAME":"新建"},{"TASK_STATUS_CODE":"RELEASED","TASK_STATUS_NAME":"已下达"},{"TASK_STATUS_CODE":"RUNNING","TASK_STATUS_NAME":"运行中"},{"TASK_STATUS_CODE":"DISPATCHED","TASK_STATUS_NAME":"已分派"},{"TASK_STATUS_CODE":"QUEUING","TASK_STATUS_NAME":"排队中"},{"TASK_STATUS_CODE":"PENDING","TASK_STATUS_NAME":"暂挂"},{"TASK_STATUS_CODE":"PAUSE","TASK_STATUS_NAME":"暂停"},{"TASK_STATUS_CODE":"CANCELLED","TASK_STATUS_NAME":"取消"},{"TASK_STATUS_CODE":"CLOSED","TASK_STATUS_NAME":"关闭"},{"TASK_STATUS_CODE":"COMPLETED","TASK_STATUS_NAME":"已完成"},{"TASK_STATUS_CODE":"EXCEPTION","TASK_STATUS_NAME":"异常"},{"TASK_STATUS_CODE":"SUSPENSED","TASK_STATUS_NAME":"暂停下发"},{"TASK_STATUS_CODE":"UNPACKING","TASK_STATUS_NAME":"拆包中"},{"TASK_STATUS_CODE":"UNPACKED","TASK_STATUS_NAME":"拆包完成"}]

# newData = [{'id': item['TASK_STATUS_CODE'], 'text': item['TASK_STATUS_NAME']} for item in data]
# print(newData)

data = {
  "createList": [
    {
      "createId": "160612",
      "creater": "欧栋利",
      "id": "160612"
    },
    {
      "createId": "170494",
      "creater": "宋小卫",
      "id": "170494"
    },
    {
      "createId": "170495",
      "creater": "王虎",
      "id": "170495"
    },
    {
      "createId": "190883",
      "creater": "徐桥军",
      "id": "190883"
    },
    {
      "createId": "200154",
      "creater": "孙全意",
      "id": "200154"
    },
    {
      "createId": "8565",
      "creater": "胡刚强",
      "id": "8565"
    },
    {
      "createId": "9739",
      "creater": "沈宇宙",
      "id": "9739"
    },
    {
      "createId": "9740",
      "creater": "白建强",
      "id": "9740"
    },
    {
      "createId": "9901",
      "creater": "杨瑞华",
      "id": "9901"
    },
    {
      "createId": "7999",
      "creater": "田进发",
      "id": "7999"
    },
    {
      "createId": "180942",
      "creater": "祝梁念",
      "id": "180942"
    },
    {
      "createId": "200703",
      "creater": "周金良",
      "id": "200703"
    },
    {
      "createId": "201967",
      "creater": "冯响雷",
      "id": "201967"
    },
    {
      "createId": "200570",
      "creater": "赵兵兵",
      "id": "200570"
    }
  ],
  "data": {
    "taskName": "巡线任务",
    "taskNum": ""
  },
  "moNumList": [
    {
      "lineCode": "WRGC-JYZLS1",
      "moNum": "MO2021050103",
      "lineName": "拉伸自动线1",
      "id": "MO2021050103"
    },
    {
      "lineCode": "WRGC-SGW2",
      "moNum": "MO2021050113",
      "lineName": "四工位机械手2",
      "id": "MO2021050113"
    },
    {
      "lineCode": "WRGC-MNJXS1",
      "moNum": "MO2021050116",
      "lineName": "模内机械手1",
      "id": "MO2021050116"
    },
    {
      "lineCode": "WRGC-CYK",
      "moNum": "MO2021050124",
      "lineName": "冲预孔自动线",
      "id": "MO2021050124"
    },
    {
      "lineCode": "WRGC-JGGM",
      "moNum": "MO2021050125",
      "lineName": "激光割膜自动线",
      "id": "MO2021050125"
    },
    {
      "lineCode": "WRGC-SKZW",
      "moNum": "MO2021050126",
      "lineName": "机器人数控折弯2连线",
      "id": "MO2021050126"
    },
    {
      "lineCode": "WRGC-JYZZD",
      "moNum": "MO2021050127",
      "lineName": "集烟罩自动线",
      "id": "MO2021050127"
    },
    {
      "lineCode": "WRGC-WZ",
      "moNum": "MO2021050128",
      "lineName": "网罩自动线",
      "id": "MO2021050128"
    },
    {
      "lineCode": "WRGC-SGW1",
      "moNum": "MO2021050129",
      "lineName": "四工位机械手1",
      "id": "MO2021050129"
    },
    {
      "lineCode": "WRGC-BJZD",
      "moNum": "MO2021050130",
      "lineName": "钣金自动线",
      "id": "MO2021050130"
    },
    {
      "lineCode": "WRGC-WGW",
      "moNum": "MO2021050131",
      "lineName": "五工位机械手",
      "id": "MO2021050131"
    },
    {
      "lineCode": "WRGC-MNJXS2",
      "moNum": "MO2021050134",
      "lineName": "模内机械手2",
      "id": "MO2021050134"
    },
    {
      "lineCode": "WRGC-LZJQR",
      "moNum": "MO2021050135",
      "lineName": "六轴机器人线",
      "id": "MO2021050135"
    },
    {
      "lineCode": "WRGC-JYZLS2",
      "moNum": "MO2021050136",
      "lineName": "拉伸自动线2",
      "id": "MO2021050136"
    },
    {
      "lineCode": "WRGC-MBDM1",
      "moNum": "MO2021050139",
      "lineName": "面板打磨自动线1",
      "id": "MO2021050139"
    },
    {
      "lineCode": "WRGC-MBDM2",
      "moNum": "MO2021050140",
      "lineName": "面板打磨自动线2",
      "id": "MO2021050140"
    }
  ],
  "liableList": [
    {
      "createId": "160612",
      "creater": "欧栋利",
      "id": "160612"
    },
    {
      "createId": "170494",
      "creater": "宋小卫",
      "id": "170494"
    },
    {
      "createId": "170495",
      "creater": "王虎",
      "id": "170495"
    },
    {
      "createId": "190883",
      "creater": "徐桥军",
      "id": "190883"
    },
    {
      "createId": "200154",
      "creater": "孙全意",
      "id": "200154"
    },
    {
      "createId": "8565",
      "creater": "胡刚强",
      "id": "8565"
    },
    {
      "createId": "9739",
      "creater": "沈宇宙",
      "id": "9739"
    },
    {
      "createId": "9740",
      "creater": "白建强",
      "id": "9740"
    },
    {
      "createId": "9901",
      "creater": "杨瑞华",
      "id": "9901"
    },
    {
      "createId": "7999",
      "creater": "田进发",
      "id": "7999"
    },
    {
      "createId": "180942",
      "creater": "祝梁念",
      "id": "180942"
    },
    {
      "createId": "200703",
      "creater": "周金良",
      "id": "200703"
    },
    {
      "createId": "201967",
      "creater": "冯响雷",
      "id": "201967"
    },
    {
      "createId": "200570",
      "creater": "赵兵兵",
      "id": "200570"
    }
  ]
}

[{'id': item['id'], 'text': item['creater']} for item in data['createList']]
# for item in data['createList']:
#   print(item['creater'])
