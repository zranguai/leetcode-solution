# 题目描述:
"""
    https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
# 相关标签: 链表 递归

# 思路:

"""
    准备临时节点dummy p
    1. 只要l1和l2不空，就把较小的值拼接到p上面来
    2. 若l1后面还不空，把l1后面的都拼接到p上面来
    3. 若l2后面还不空，把l2后面的都拼接到p上面来
"""

# 运行结果: 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了96.27%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了57.24%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # 虚拟头节点，避免处理空指针情况
        p = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next  # p 指针不断前进
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next


if __name__ == '__main__':
    pass
