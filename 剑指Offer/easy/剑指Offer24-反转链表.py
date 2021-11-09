# 题目描述
"""
    https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""
# 相关标签: 链表
# 思路:
"""
    1. 新建一个含头节点的空链表
    2. 依次遍历目标链表
    3. 采用头插法进行插入
"""
# 执行结果: 超出时间限制
"""
    
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while head:
            # 保存下一个
            tmp = head.next
            # 采用头插法将 head 放入到 newHead 的头部
            # newHead.val = head.val
            head.next = newHead
            newHead = head
            print(newHead)

            # 下一个
            head = tmp

            # 继续遍历原链表的下一个
        return newHead


# 方法2
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre




