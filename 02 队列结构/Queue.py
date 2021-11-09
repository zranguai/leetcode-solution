# 队列的实现
"""
尾部(-->进)  ----------------  头部(-->出)
             ----------------
"""
class Queue:
    def __init__(self):
        self.items = []

    # 1. 在队列的尾部添加一个元素
    def enqueue(self, item):
        self.items.insert(0, item)

    # 2. 从队列的头部删除一个元素
    def dequeue(self):
        return self.items.pop()

    # 3. 检查队列是否为空
    def isEmpty(self):
        return self.items == []

    # 4. 返回队列中元素的个数
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    # 测试:
    q = Queue()
    print(q.isEmpty())
    q.enqueue('dog')
    q.enqueue(4)
    print(q.isEmpty())

    q.enqueue(True)

    print(q.dequeue())
    print(q.size())
    print(q.items)



