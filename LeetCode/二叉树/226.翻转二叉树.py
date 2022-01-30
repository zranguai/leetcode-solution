# 题目描述:
"""
    https://leetcode-cn.com/problems/invert-binary-tree/
"""
# 相关标签: 二叉树 深度优先搜索 广度优先搜索 树

# 思路:
"""
    调换左右节点在前序位置和后序位置都可以
"""

# 运行结果:
"""
    执行用时：16 ms, 在所有 Python 提交中击败了76.84%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了56.02%的用户
    通过测试用例：77 / 77
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == '__main__':
    pass
