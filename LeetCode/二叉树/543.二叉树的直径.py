# 题目描述:
"""
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
"""
# 相关标签: 二叉树 深度优先搜索 树

# 思路:
"""
    在后序位置操作，使用全局变量记录整棵树的最大直径
"""

# 运行结果:
"""
    执行用时：36 ms, 在所有 Python 提交中击败了21.97%的用户
    内存消耗：15.8 MB, 在所有 Python 提交中击败了59.09%的用户
    通过测试用例：104 / 104
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxDiameter = 0  # 全局变量

    def maxDepth(self, root):
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 在后序位置上
        myDiameter = left + right
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxDepth(root)
        return self.maxDiameter


if __name__ == '__main__':
    pass
