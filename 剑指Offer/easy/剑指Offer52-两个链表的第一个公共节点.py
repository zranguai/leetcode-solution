# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
"""
# 标签: 哈希表 链表 双指针


# 方法一
# 解题思路:
"""
    step1: 先分别统计两个链表的长度
    step2: 链表长的先走，两个同时长是同时走，走到相交点位置停止
"""

# 执行结果：解答错误，通过测试用例 33 / 45
"""
最后执行的输入：
3
[3]
[2,3]
0
1
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB
        nump = 0
        numq = 0
        if p == q:
            return p
        while p != None:
            nump += 1
            p = p.next
        while q != None:
            numq += 1
            q = q.next

        if nump < numq:
            sub = numq - nump
            p_ = headA
            q_first = headB
            while sub > 0:
                sub -= 1
                q_first = q_first.next
            while p_.next != q_first.next:
                p_ = p_.next
                q_first = q_first.next
            if p_.next == q_first.next:
                return f"Intersected at '{p_.next.val}'"
            else:
                return None
        else:
            sub = nump - numq
            p_ = headB
            q_first = headA
            while sub > 0:
                sub -= 1
                q_first = q_first.next
            while p_.next != q_first.next:
                p_ = p_.next
                q_first = q_first.next
            if p_.next == q_first.next:
                return f"Intersected at '{p_.next.val}'"
            else:
                return None



# 方法二:

# 解题思路
"""
    双指针法
    stpe1: 设置两个指针nodeA,刚开始指向headA
                     nodeB,刚开始指向headB
    step2: 只要两个指针相遇，就同时向后走， 当其中一个走到最后是，指针进行交换
"""

# 执行结果: 通过
"""
执行用时：160 ms, 在所有 Python 提交中击败了34.21% 的用户
内存消耗：42.1 MB, 在所有 Python 提交中击败了91.25% 的用户
通过测试用例：45 / 45
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA






if __name__ == '__main__':
    pass