# 题目描述
"""
    https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
"""
# 相关标签: 分治算法
# 思路
"""
    1. 先创建一个空的链表cur=dum=ListNode(0)
    2. 如果l1上的数字小就把l1上的,cur走一步, l2的同理可得
    3. 到最后l1为空或者l2为空停止
    4. 将最后没空的再拼接到后面
    5. 返回dum.next
"""
# 执行结果
"""
执行用时：36 ms, 在所有 Python 提交中击败了94.90%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了85.03%的用户
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        return dum.next




