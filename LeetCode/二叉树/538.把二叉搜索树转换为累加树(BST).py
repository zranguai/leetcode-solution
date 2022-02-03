# 题目描述:
"""
    https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
"""
# 相关标签: 二叉搜索树 二叉树 树 深度优先搜索

# 思路:
"""
    还是根据二叉搜索树中序遍历出来的结果是从小到大的结论
    这里需要得到从达到小的结果
    1. 先遍历右子树
    2. 将结果往前一个节点加
    3. 遍历左子树
"""

# 运行结果:
"""
    执行用时：60 ms, 在所有 Python 提交中击败了48.37%的用户
    内存消耗：17.2 MB, 在所有 Python 提交中击败了83.74%的用户
    通过测试用例：215 / 215
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0

    def traverse(self, root):
        if root == None:
            return
        self.traverse(root.right)
        # 维护累加和
        self.sum += root.val
        # 变成累加树
        root.val = self.sum
        self.traverse(root.left)

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.traverse(root)
        return root





