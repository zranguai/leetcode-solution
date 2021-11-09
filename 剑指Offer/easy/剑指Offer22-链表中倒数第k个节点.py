# 题目描述
"""
    https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""
# 相关标签: 链表, 双指针
# 思路
"""
    使用双指针，start = self.head, end = self.head
    先让end走k个节点
    然后start和end同时走, 直到end走到了None
    最后start指向的就是要返回节点的头节点
"""
# 执行结果: 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了94.69%的用户
    内存消耗：12.9 MB, 在所有 Python 提交中击败了74.78%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = head
        end = head
        # 先让end走k个节点
        for i in range(k):
            end = end.next

        # 同时走
        while end != None:
            start = start.next
            end = end.next

        return start