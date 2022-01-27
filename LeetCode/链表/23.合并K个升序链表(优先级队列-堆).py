# 题目描述:
"""
    https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
# 相关标签: 链表 递归

# 思路:

"""
    暂时还不太懂堆的原理
"""

# 运行结果: 通过
"""
    执行用时：60 ms, 在所有 Python 提交中击败了71.50%的用户
    内存消耗：18.6 MB, 在所有 Python 提交中击败了51.83%的用户
    通过测试用例：133 / 133
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))  # 将值加入head中，保持堆的不变性
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)  # 弹出并返回head的最小的元素
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next



if __name__ == '__main__':
    pass
