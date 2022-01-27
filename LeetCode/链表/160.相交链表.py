# 题目描述:
"""
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
"""
# 相关标签: 链表 递归

# 思路:

"""
    1. 先依次遍历两个链表，得到两个链表的长度lenA, lenB
    2. 较长的链表先走(lenB-lenA)
    3. 两个链表同时走，直到遇见相交值
"""

# 运行结果: 通过
"""
    执行用时：140 ms, 在所有 Python 提交中击败了92.39%的用户
    内存消耗：42.4 MB, 在所有 Python 提交中击败了25.14%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """


if __name__ == '__main__':
    pass
