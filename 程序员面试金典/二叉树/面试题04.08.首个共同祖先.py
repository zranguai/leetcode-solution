# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/first-common-ancestor-lcci/
"""
# 相关标签: 树 深度优先搜索 二叉树
# 思路:
"""
    在前序遍历的位置进行判断并返回p/q节点
    
    在后续位置(离开节点)进行判断根节点的左右包含或者等于p/q
"""
# 执行结果
"""
    执行用时：44 ms, 在所有 Python 提交中击败了96.15%的用户
    内存消耗：24.6 MB, 在所有 Python 提交中击败了80.77%的用户
    通过测试用例：31 / 31
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root == p or root == q: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 都为空
        if left == None and right == None:
            return None
        # 都不空
        if left and right:
            return root
        # 其中一个为空
        return left if left else right


if __name__ == '__main__':
    pass
