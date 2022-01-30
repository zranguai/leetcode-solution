# 题目描述:
"""
    https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
# 相关标签: 二叉树 深度优先搜索 栈 树

# 思路:
"""
    使用递归执行前序遍历
"""

# 运行结果:
"""
    执行用时：16 ms, 在所有 Python 提交中击败了64.55%的用户
    内存消耗：12.9 MB, 在所有 Python 提交中击败了89.72%的用户
    通过测试用例：69 / 69
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归方法使用前序遍历
        if root == None:
            return
        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.res


if __name__ == '__main__':
    pass
