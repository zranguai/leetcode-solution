# 题目描述:
"""
    https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
# 相关标签: 快慢双指针 链表 哈希表

# 思路:
"""
    通过化示意图可得，
    快指针fast和慢指针第一次相遇后，从相遇点走到环的第一个节点
    和从头走到环的第一个节点所需的路径相同所以：
    无环返回null
    1. 先找到快慢指针相遇点 同141题
    2. 将其中一个指针防止到头指针
    3. 两个指针同步走，再次相遇的时候就是环的第一个节点
"""

# 运行结果:
"""
    执行用时：36 ms, 在所有 Python 提交中击败了84.73%的用户
    内存消耗：20 MB, 在所有 Python 提交中击败了43.50%的用户
    通过测试用例：21 / 21
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while True:
            if not (fast and fast.next): return  # 特殊情况退出
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break  # 找到快慢指针相遇点 同141题

        fast = head  # 其中一个指针防止到头指针
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast

if __name__ == '__main__':
    pass
