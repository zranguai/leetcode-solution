# 题目描述
"""
    https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
"""
# 相关标签：链表
# 思路:
"""
    step1: 设置两个指针1.previous = none  2. current = self.head
    step2: 从头节点依次找你要的值,找到后将该值删除掉
    step3：注意还要分删除的是不是第一个值
"""
# 执行结果
"""
    执行用时：32 ms, 在所有 Python 提交中击败了27.91%的用户
    内存消耗：13.4 MB, 在所有 Python 提交中击败了24.48%的用户

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        previous = None
        current = head
        while current.val != val:    # 查找该节点
            previous = current
            current = current.next

        # 删除该节点
        if current == head:  # 头节点情况
            head = current.next
        else:  # 其他情况
            previous.next = current.next
        return head


# 测试
if __name__ == '__main__':
    pass