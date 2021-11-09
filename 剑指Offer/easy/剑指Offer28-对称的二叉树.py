# 题目描述
"""
    https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
"""
# 相关标签: 树
# 解题思路
"""
    0. 当为空树的时候成立
    1. 将其看成两个子树
    2. 当里面的函数传入左子树和右子树
    3. 当两棵树同时为空的时候返回true
    4. 当两棵树不同时为空或者两棵树里的值不同的时侯返回false
"""
# 执行结果
"""
    执行用时：24 ms, 在所有 Python 提交中击败了67.12%的用户
    内存消耗：13 MB, 在所有 Python 提交中击败了91.67%的用户
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Symmetric(L, R):
            if not L and not R:
                return True
            if not L or not R or L.var != R.val:
                return False

            return Symmetric(L.left, R.right) and Symmetric(L.right, R.left)

        return Symmetric(root.left, root.right) if root else True