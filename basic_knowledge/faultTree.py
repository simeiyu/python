tree_data = {
    "attr": {"width": 1920, "height": 1080, "background": "#fff", "fontColor": "#000", "eventColor": "#000", "gateColor": "#000", "eventCode": True, "eventProbability": False, "containerX": 0, "containerY": 0},
    "eventList": [
        {"type": "1", "name": "顶层事件", "code": "T1", "id": "event-765d3f8a173b4ea097b1cb4e02d4a285"}, {"id": "event-59156103ab7f4adf86067a8d55247a8d", "type": "2",
                                                                                                      "name": "事件1", "code": "code1"}, {"id": "event-386b6feeeeb94583be2b68f24c870e81", "type": "3", "name": "事件2", "code": "code2", "eventProbability": 1}
    ],
    "nodeList": [
        {"type": "1", "gate": "1", "eventModel": "event-765d3f8a173b4ea097b1cb4e02d4a285", "x": 526, "y": 38, "id": "node-43959637fde04ef680e1cb73d85b05a4", "transfer": ""}, {"type": "2", "eventModel": "event-59156103ab7f4adf86067a8d55247a8d", "gate": "1", "x": 426, "y": 188, "id": "node-a558d0fd5ea44b579c3716e71d53e070", "transfer": ""}, {"type": "3", "eventModel": "event-386b6feeeeb94583be2b68f24c870e81", "gate": "1", "x": 581, "y": 189, "id": "node-2dea27c81dfb431a8c523e2d0ab4550f", "transfer": ""}, {
            "type": "5", "eventModel": "event-386b6feeeeb94583be2b68f24c870e81", "gate": "1", "x": 681, "y": 188, "id": "node-62d75afe672f4a53a3cdc43d2f255fc7", "transfer": ""}, {"type": "4", "eventModel": "event-386b6feeeeb94583be2b68f24c870e81", "gate": "1", "x": 646, "y": 88, "id": "node-57473302804148f0884e43469bfe0537", "transfer": ""}, {"type": "3", "eventModel": "event-386b6feeeeb94583be2b68f24c870e81", "gate": "1", "x": 326, "y": 338, "id": "node-d89ee146bdb649439ebeb484167e6f64", "transfer": ""}
    ],
    "linkList": [{"type": "link", "id": "link-aebb78deb2e3425081a6a5486d3f8848", "sourceId": "node-a558d0fd5ea44b579c3716e71d53e070", "targetId": "node-43959637fde04ef680e1cb73d85b05a4", "isCondition": False}, {"type": "link", "id": "link-c7ef294a9e9e439489d8746294e24c59", "sourceId": "node-2dea27c81dfb431a8c523e2d0ab4550f", "targetId": "node-43959637fde04ef680e1cb73d85b05a4", "isCondition": False}, {"type": "link", "id": "link-eccd3940239f4099a44bc69c3d9f4860", "sourceId": "node-62d75afe672f4a53a3cdc43d2f255fc7", "targetId": "node-43959637fde04ef680e1cb73d85b05a4", "isCondition": False}, {"type": "link", "id": "link-101f4280803e4032b38aaa82ad28ff45", "sourceId": "node-57473302804148f0884e43469bfe0537", "targetId": "node-43959637fde04ef680e1cb73d85b05a4", "isCondition": True}, {"type": "link", "id": "link-c51e59c1ff694b1184834103765110f9", "sourceId": "node-d89ee146bdb649439ebeb484167e6f64", "targetId": "node-a558d0fd5ea44b579c3716e71d53e070", "isCondition": False}]}

GateMap = {
  "1": "0", 
  "2": "1",
  "3": "0",
}

def findEvent(list, key, val):
    for item in list:
        if item[key] == val:
            return item


def findNodeId(list, key1, val, key2):
    for item in list:
        if item[key1] == val:
            return item[key2]


def findNodesId(list, key1, val, key2):
    ids = []
    for item in list:
        if item[key1] == val:
            ids.append(item[key2])
    return ids


def fault_tree(data):
    nodeList = data['nodeList']
    eventList = data['eventList']
    linkList = data['linkList']
    topEvent = findEvent(eventList, 'type', '1')
    # rootNode = {}
    nodes = []
    for item in nodeList:
        event = findEvent(eventList, 'id', item['eventModel'])
        ParentNode = findNodeId(linkList, 'sourceId', item['id'], 'targetId')
        ChildrenNode = findNodesId(
            linkList, 'targetId', item['id'], 'sourceId')
        IsRoot = 0
        IsLeaf = 0
        HasNoGate = 0
        Probability = 0
        LogicSymbol = "3"
        if 'gate' in item:
          LogicSymbol = GateMap[item['gate']]
        if item['eventModel'] == topEvent['id']:
            IsRoot = 1
        if len(ChildrenNode) > 0:
            IsLeaf = 1
        if 'hasNotGate' in item and item['hasNotGate']:
            HasNoGate = 1
        if 'eventProbability' in event:
          Probability = event['eventProbability'] / 100
        node = {
            'Gid': item['id'],
            'ParentNode': ParentNode,
            'ChildrenNode': ChildrenNode,
            'IsRoot': IsRoot,
            'IsLeaf': IsLeaf,
            'HasNoGate': HasNoGate,
            'LogicSymbol': LogicSymbol,
            'NodeName': event['name'],
            'EventNumber': event['id'],
            'Probability': Probability
        }
        if item['eventModel'] == topEvent['id']:
            rootNode = node
        nodes.append(node)

    return {
        'rootNode': rootNode,
        'nodes': nodes
    }


data = fault_tree(tree_data)
print(data)
