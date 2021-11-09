from Node import Node


# tips:在python中None可以和任何引用进行比较
# 无序列表--unordered list
class UnorderedList:
    def __init__(self):
        self.head = None  # 这个可以理解为头节点

    # 1.判断链表是不是空
    def isEmpty(self):
        return self.head == None

    # 2.添加元素
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # 将后面的元素给temp-->这步和下步的顺序特别重要,调换将导致头节点指向空
        self.head = temp  # 将头节点连接到temp

    # 3.返回链表的长度
    def length(self):
        current = self.head
        count = 0  # 进行计数
        while current != None:
            count += 1
            current = current.getNext()
        return count

    # 4.在无序列表中搜索一个值
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    # 5.移除链表中的元素
    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == Node:
            self.head = current.getNext()  # 如果删除的是第一个节点
        else:
            previous.setNext(current.getNext())

    # 6.向链表的最后插入元素
    def append(self, item):
        temp = Node(item)
        current = self.head
        found = False
        while current != None and not found:
            if current.getNext() == None:
                temp.setNext(None)
                current.setNext(temp)
                found = True
            else:
                current = current.getNext()
        if self.head == None:
            temp.setNext(self.head)
            self.head = temp

    # 7.向链表中插入元素
    def insert(self, item, ind):
        if ind > self.length() - 1:
            return False
        else:
            temp = Node(item)
            current = self.head
            previous = None
            found = False
            count = 0  # 用于计数是否到了ind
            if ind == 0:  # 考虑在头节点的后面插入元素
                temp.setNext(self.head)
                self.head = temp
            else:
                while current != None and not found:  # 这里排除了在头节点插入的情况
                    if count == ind:
                        temp.setNext(current)
                        previous.setNext(temp)
                        found = True
                    else:
                        count += 1
                        previous = current
                        current = current.getNext()

    # 8.返回该位置上的元素
    def index(self, ind):
        pass

    # 9. 弹出元素
    def pop(self, ind):
        pass

    # 遍历查看链表---->该方法用于验证自己的代码是否写对了
    def look(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


# 测试
if __name__ == '__main__':
    # 1. Node测试
    # temp1 = Node(1)
    # temp2 = Node(2)
    # temp3 = Node(3)
    # temp1.setNext(temp2)
    # temp2.setNext(temp3)
    # print(temp1.getData())
    # print(temp1.getNext().getNext().getData())
    # 2.UnorderedList测试
    mylist = UnorderedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    # mylist.append(11)
    # mylist.remove(2)
    # print(mylist.search(2))
    # print(mylist.length())
    # print(mylist.head.getData())
    # print(mylist.length())
    # mylist.look()  # 3, 2, 1
    # mylist.insert(5, 1)
    # mylist.insert(4, 1)
    # mylist.insert(6, 0)
    mylist.look()
