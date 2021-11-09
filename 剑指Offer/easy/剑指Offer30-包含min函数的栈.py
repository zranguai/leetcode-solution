# 题目描述
"""
    https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/submissions/
"""
# 相关标签: 栈, 设计
# 解题思路
"""
    利用栈的定义即可
"""
# 执行结果
"""
    执行用时：552 ms, 在所有 Python 提交中击败了12.93%的用户
    内存消耗：16.8 MB, 在所有 Python 提交中击败了34.8%的用户
"""

# 方法1: 直接法

class MinStack1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        self.Stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.Stack[-1]



    def min(self):
        """
        :rtype: int
        """
        return min(self.Stack)



# 方法2：使用辅助栈: 空间换时间
"""
    执行用时：164 ms, 在所有 Python 提交中击败了22.67%的用户
    内存消耗：16.5 MB, 在所有 Python 提交中击败了92.67%的用户
"""
class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack_A, self.Stack_B = [], []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.Stack_A.append(x)
        if not self.Stack_B or x > self.Stack_B[-1]:
            self.Stack_B.append(-1)


    def pop(self):
        """
        :rtype: None
        """
        if self.Stack_A.pop() > self.Stack_B[-1]:
            self.Stack_B.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.Stack_A[-1]



    def min(self):
        """
        :rtype: int
        """
        return self.Stack_B[-1]


if __name__ == '__main__':
    stack = MinStack2()
    stack.push(-2)
    stack.push(3)
    print(stack.Stack_A)
    print(stack.top())
    print(stack.min())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()