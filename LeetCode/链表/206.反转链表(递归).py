# 题目描述:
"""

"""
# 相关标签: 递归 链表

# 思路:

"""
    通过递归来进行反转链表
    考虑递归反过来倒数第二层情况
"""

# 运行结果: 通过
"""
    执行用时：44 ms, 在所有 Python 提交中击败了11.87%的用户
    内存消耗：18.1 MB, 在所有 Python 提交中击败了18.76%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


if __name__ == '__main__':
    pass
