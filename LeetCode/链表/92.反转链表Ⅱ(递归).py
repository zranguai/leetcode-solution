# 题目描述:
"""
    https://leetcode-cn.com/problems/reverse-linked-list-ii/
"""
# 相关标签: 递归 链表

# 思路:

"""
    https://labuladong.gitee.io/algo/2/17/17/
"""

# 运行结果: 通过
"""
    执行用时：24 ms, 在所有 Python 提交中击败了9.30%的用户
    内存消耗：13.7 MB, 在所有 Python 提交中击败了5.15%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.successor = None

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)  # 反转前right个链表
        head.next = self.reverseBetween(head.next, left - 1, right - 1)  # 保证left前面的不要动
        return head



if __name__ == '__main__':
    pass
