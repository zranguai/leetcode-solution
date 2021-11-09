# 题目描述
"""
    https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
"""
# 相关标签: 树
# 思路
"""
    采用遍历的思想,如果根节点是空就返回
    1. 采用临时节点存储
    2. 依次遍历交换左右子树
    3. 最后返回根节点
"""
# 执行结果
"""
    执行用时：24 ms, 在所有 Python 提交中击败了33.80%的用户
    内存消耗：12.8 MB, 在所有 Python 提交中击败了89.68%的用户
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return

        temp = root.left

        root.left = self.mirrorTree(root.right)

        root.right = self.mirrorTree(temp)

        return root