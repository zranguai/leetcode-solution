# 题目描述:
"""
    https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
"""
# 相关标签: 二叉搜索树 二叉树 树

# 思路:
"""
    先找到该位置，然后在该位置上插入目标元素

"""

# 运行结果:
"""
    执行用时：80 ms, 在所有 Python 提交中击败了42.68%的用户
    内存消耗：17 MB, 在所有 Python 提交中击败了58.54%的用户
    通过测试用例：35 / 35
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    pass
