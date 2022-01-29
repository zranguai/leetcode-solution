# 题目描述:
"""
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""
# 相关标签: 递归 链表

# 思路:

"""
    https://labuladong.gitee.io/algo/2/17/18/
"""

# 运行结果: 通过
"""
    执行用时：40 ms, 在所有 Python 提交中击败了12.79%的用户
    内存消耗：15 MB, 在所有 Python 提交中击败了13.09%的用户
    通过测试用例：208 / 208
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 反转以 a 为头结点的链表
    def reverse_a(self, a):
        pre, cur, nxt = None, a, a
        while cur != None:
            nxt = cur.next
            # 逐个节点翻转
            cur.next = pre
            # 更新指针位置
            pre = cur
            cur = nxt
        # 返回翻转后的头节点
        return pre

    # 翻转[a, b)的元素，
    def reverse_ab(self, a, b):
        pre, cur, next = None, a, a
        while cur != b:
            nxt = cur.next
            # 逐个翻转链表
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        a = b = head
        for i in range(k):
            # 不足 k 个，不需要反转，base case
            b = b.next
        # 反转前 k 个元素
        newHead = self.reverse_ab(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return newHead

if __name__ == '__main__':
    pass
    import copy
    copy.deepcopy()
