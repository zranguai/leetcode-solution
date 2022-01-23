# 题目描述:
"""
    https://leetcode-cn.com/problems/middle-of-the-linked-list/
"""
# 相关标签: 快慢双指针 链表

# 思路:
"""
    1. 使用快慢双指针
    2. 快指针走两步慢指针走一步
    3. 当快指针走到头后慢指针指向中点
"""

# 运行结果: 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了64.37%的用户
    内存消耗：13 MB, 在所有 Python 提交中击败了85.79%的用户
    通过测试用例：36 / 36
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    pass
