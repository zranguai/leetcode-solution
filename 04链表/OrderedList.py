from Node import Node

# 有序列表
class OrderedList:
    def __init__(self):
        self.head = None

    # 1. 向链表中添加元素
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # 2. 假设item已经在列表中,并从中移除item
    def remove(self, item):
        pass

    # 3.在列表中搜索item--->返回bool值
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    # 4. 检查列表是否为空--->返回bool值
    def isEmpty(self):
        pass

    # 5. 返回链表中元素的个数
    def length(self):
        pass

    # 6. 假设item已经在列表中,并返回该元素在列表中的位置
    def index(self, item):
        pass

    # 7. 假设列表不为空,并移除列表中的最后一个元素
    def pop(self):
        pass

    # 8. 假设在指定的位置pos存在元素,并移除该位置上的元素--->他接受位置参数，并返回一个元素
    def pop(self, pos):
        pass


if __name__ == '__main__':
    mylist = OrderedList()
    mylist.add(1)
    mylist.add(6)
    mylist.add(5)
    mylist.add(4)