# 题目描述
"""
https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""
# 相关标签: 栈/设计
# 思路:
"""
    1.准备两个栈A和B
    2.要是appendTail-->就向A中添加元素
    3.要是deleteHead
            1.B为空-->依次循环将A(不为空)中元素添加到B中来最后再B.pop()  ，A为空返回-1
            2.B不为空-->进行B.pop()
"""
# 执行结果:通过
"""
执行用时：1480 ms, 在所有 Python 提交中击败了70.29%的用户
内存消耗：17.6 MB, 在所有 Python 提交中击败了18.43%的用户
"""


class CQueue(object):

    def __init__(self):
        self.A = []
        self.B = []


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.A.append(value)



    def deleteHead(self):
        """
        :rtype: int
        """
        if self.B:  # B不为空的情况
            return self.B.pop()
        elif not self.A:  # A中为空的情况
            return -1
        else:
            while self.A:
                self.B.append(self.A.pop())
            return self.B.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

