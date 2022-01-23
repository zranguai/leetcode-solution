"""
我把双指针技巧再分为两类，一类是「快慢指针」，一类是「左右指针」。
前者解决主要解决链表中的问题，比如典型的判定链表中是否包含环；
后者主要解决数组（或者字符串）中的问题，比如二分查找。
"""
# 题目描述:
"""
    https://leetcode-cn.com/problems/linked-list-cycle/
"""
# 相关标签: 快慢双指针 链表 哈希表

# 思路:
"""
    fast比slow每次多走一步，如果有环一定会相遇
"""

# 运行结果:
"""
    执行用时：24 ms, 在所有 Python 提交中击败了99.05%的用户
    内存消耗：19.1 MB, 在所有 Python 提交中击败了51.81%的用户
    通过测试用例：16 / 16
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 使用快慢双指针
        fast = head
        slow = head
        while fast and fast.next:
            # fast比slow每次多走一步，如果有环一定会相遇
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

if __name__ == '__main__':
    pass
