# 题目描述
"""
    https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""
# 相关标签: 链表
# 思路:
"""
    依次从头开始遍历链表，并使用列表(数组)临时存储起来
    最后再将列表(数组)翻转即可
"""
# 执行结果: 通过
"""
执行用时:28ms,在所有 Python 提交中击败了61.18%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了99.85%的用户
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, alist):
        alist.reverse()
        return alist
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        temp = []
        current = head
        while current != None:
            temp.append(current.val)
            current = current.next
        return self.reverse(temp)



# 测试:
if __name__ == '__main__':
    solution = Solution()
    head = [1, 3, 2]
    print(solution.reversePrint(head))
