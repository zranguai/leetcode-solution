# 1.创建Node类--->将next值初始化为None
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # 1.得到该节点的数据
    def getData(self):
        return self.data

    # 2. 得到该节点的next
    def getNext(self):
        return self.next

    # 3.设置该节点的值
    def setData(self, newdata):
        self.data = newdata

    # 4.设置该节点的next
    def setNext(self, newnext):
        self.next = newnext

