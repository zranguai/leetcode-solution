# 03双端队列
"""
 后端-------------------------前端
    -------------------------
"""
class Deque:
    def __init__(self):
        self.items = []

    # 1.将一个元素添加到双端队列的前端
    def addFront(self, item):
        self.items.append(item)

    # 2.将一个元素添加到双端队列的后端
    def addRear(self, item):
        self.items.insert(0, item)

    # 3.从双端队列的前端移除一个元素
    def removeFront(self):
        return self.items.pop()

    # 4.从双端队列的后端移除一个元素
    def removeRear(self):
        return self.items.pop(0)

    # 5.检查双端队列是否为空
    def isEmpty(self):
        return self.items == []

    # 6.返回双端队列中元素的数目
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    # 测试
    d = Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())




