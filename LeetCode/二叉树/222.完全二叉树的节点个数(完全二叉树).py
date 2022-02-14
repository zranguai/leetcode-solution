# 题目描述:
"""
    https://leetcode-cn.com/problems/count-complete-tree-nodes/
"""
# 相关标签: 深度优先搜索 二叉树 树 二分查找

# 方法1：
# 思路:
"""
    直接把他看成一棵普通二叉树进行计算节点
"""

# 运行结果:
"""
    执行用时：72 ms, 在所有 Python 提交中击败了32.34%的用户
    内存消耗：28.1 MB, 在所有 Python 提交中击败了100.00%的用户
    通过测试用例：18 / 18
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right


# 方法2：
# 思路:
"""
    把完全二叉树一部分看作是满二叉树，一部分看作是普通二叉树
    满二叉树计算方法: 2**h - 1
    时间复杂度O(logN * logN)
"""

# 运行结果:
"""
    执行用时：56 ms, 在所有 Python 提交中击败了81.65%的用户
    内存消耗：28.3 MB, 在所有 Python 提交中击败了82.57%的用户
    通过测试用例：18 / 18
"""


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l, r = root, root
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        # 如果是满二叉树，把他看作满二叉树考虑
        if hl == hr:
            return 2 ** hl - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == '__main__':
    pass
