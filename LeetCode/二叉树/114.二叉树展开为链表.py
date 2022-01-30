# 题目描述:
"""
    https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
"""
# 相关标签: 二叉树 深度优先搜索 广度优先搜索 树 栈 链表

# 思路:
"""
    1. 先将左子树，右子树拉平 left = root.left right = root.right
    2. root.left = None, root.right = left(左子树放到右边)
    3. 遍历p.right 将右边的接上去
    
"""

# 运行结果:
"""
    执行用时：24 ms, 在所有 Python 提交中击败了53.30%的用户
    内存消耗：13.3 MB, 在所有 Python 提交中击败了71.66%的用户
    通过测试用例：59 / 59
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """


if __name__ == '__main__':
    pass
