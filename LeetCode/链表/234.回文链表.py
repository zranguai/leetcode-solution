# 题目描述:
"""
    https://leetcode-cn.com/problems/palindrome-linked-list/
"""
# 相关标签: 递归 链表 栈 双指针

# 思路:
# 方法1：
"""
    1. 先将该链表进行翻转
    2. 两个链表依次遍历，判断是否相等
    3. 注意需要使用深拷贝，要不然改动一个链表例外一个也会变
"""

# 运行结果: 超出时间限制
"""
    81 / 85 个通过测试用例
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1(object):
    # 翻转链表
    def reverse(self, a):
        pre, cur, nxt = None, a, a
        while cur:
            nxt = cur.next
            # 逐个节点翻转
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        import copy
        p1 = head
        p2_temp = copy.deepcopy(head)
        p2 = self.reverse(p2_temp)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


# 方法2：使用递归
# 思路
"""
    链表也有前序遍历和后续遍历
    void traverse(ListNode head) {
        // 前序遍历代码
        traverse(head.next);
        // 后序遍历代码
    }
"""
# 运行结果: 超出时间限制
"""
    执行用时：1452 ms, 在所有 Python 提交中击败了9.63%的用户
    内存消耗：123.5 MB, 在所有 Python 提交中击败了6.71%的用户
    通过测试用例：86 / 86
"""

class Solution(object):
    # 方法2
    def __init__(self):
        self.left = None

    def reverse(self, right):
        if right == None: return True
        res = self.reverse(right.next)
        # 后续遍历
        res = res and (right.val == self.left.val)
        self.left = self.left.next
        return res

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.left = head
        return self.reverse(head)


if __name__ == '__main__':
    pass
