# 栈顶端的元素位于最右侧
"""
|-----------
|-----------
"""
class Stack:
    def __init__(self):
        self.items = []

    # 1. 将原素压入栈
    def push(self, element):
        self.items.append(element)

    # 2. 从栈中取出元素
    def pop(self):
        return self.items.pop()

    # 3. 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 4. 判断是否为空
    def isEmpty(self):
        return self.items == []

    # 5. 返回栈中的元素的数目
    def size(self):
        return len(self.items)

# 进行测试
# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# 也可以选择将列表的头部作为栈的顶端---这种方式性能不好,insert(0)和pop(0)需要O(n)
"""
-----------|
-----------|
"""
# 使用pop方法和insert方法显示地访问下标为0的元素
class Stack1:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def push(self, element):
        self.items.insert(0, element)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)













