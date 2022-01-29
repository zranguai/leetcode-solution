# 题目描述:
"""
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
"""
# 相关标签: 二叉树 深度优先搜索 广度优先搜索 树

# 方法1：遍历一遍二叉树
# 思路:
"""
    遍历一遍二叉树，用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度
    考虑二叉树的时候以节点来进行考虑
    先序位置时该节点的   depth++
    后序位置时离开该节点 depth--
"""

# 运行结果:
"""
    执行用时：32 ms, 在所有 Python 提交中击败了20.88%的用户
    内存消耗：15.5 MB, 在所有 Python 提交中击败了99.03%的用户
    通过测试用例：39 / 39
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def __init__(self):
        self.res = 0
        self.depth = 0

    def traverse(self, root):
        if root == None:
            self.res = max(self.res, self.depth)
            return
        # 前序位置
        self.depth += 1
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.depth -= 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)  # 调用遍历函数
        return self.res


# 方法2：分解问题计算答案
# 思路:
"""
    通过分解问题计算答案
"""

# 运行结果:
"""
    执行用时：24 ms, 在所有 Python 提交中击败了76.52%的用户
    内存消耗：15.5 MB, 在所有 Python 提交中击败了95.68%的用户
    通过测试用例：39 / 39
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        res = max(left, right) + 1
        return res


if __name__ == '__main__':
    pass
