# 题目描述:
"""
    https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""
# 相关标签: 快慢双指针 链表

# 思路:
"""
    1. 使用快慢双指针
    2. 快指针fast先走n步
    3. 快慢指针一起走，直到fast指针指向None,此时慢指针slow指向的值就是要删除的结点
    
"""

# 运行结果: 通过
"""
    执行用时：36 ms, 在所有 Python 提交中击败了6.74%的用户
    内存消耗：12.9 MB, 在所有 Python 提交中击败了94.60%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = head, head
        for i in range(n):  # 快指针先走n步
            fast = fast.next

        if fast == None: return head.next  # 特殊情况

        while fast and fast.next:  # 快慢指针一起走, 找到要删除节点的前一个位置
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next  # 删除slow节点后的那个节点
        return head

if __name__ == '__main__':
    pass
