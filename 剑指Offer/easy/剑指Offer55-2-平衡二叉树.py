# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
"""
# 标签: 树 深度优先搜索 二叉树

# 方法1 -- 先序遍历 + 深度判断 (从顶置底)
# 解题思路:
"""
  使用先序遍历 + 判断深度(从顶至底)
  判断当前节点 abs(self.depth(root.left) - self.depth(root.right)) <= 1
  判断左子树   self.isBalanced(root.left)
  判断右子树   self.isBalanced(root.right)
"""

# 执行结果： 通过
"""
    执行用时：36 ms, 在所有 Python 提交中击败了67.84% 的用户
    内存消耗：14.5 MB, 在所有 Python 提交中击败了99.38% 的用户
    通过测试用例：227 / 227
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):  # 使用前序遍历 + 深度判断
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True  # root为空节点，返回True

        if abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
                root.right):
            return True
        else:
            return False

    def depth(self, root):
        if not root: return 0
        queue = [root]
        res = 0
        while queue:  # 每个while，走动一层
            temp = []  # 存储每一层节点
            for value in queue:
                # print(value.val)
                if value.left: temp.append(value.left)
                if value.right: temp.append(value.right)
            queue = temp
            res += 1
        return res



# 方法2
# 解题思路
"""
    后序遍历， 从低到顶
    root(左/右)深度<=1 返回子树高度 max(left, right) + 1
    root(左/右)深度>=2 返回-1
    root为空 return 0
    
"""
# 执行结果
"""
    执行用时：28 ms, 在所有 Python 提交中击败了91.55% 的用户
    内存消耗：18.2 MB, 在所有 Python 提交中击败了51.96% 的用户
    通过测试用例：227 / 227
"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def postorder(root):
            if not root: return 0
            left = postorder(root.left)
            if left == -1: return -1  # 遇到不平衡情况就返回-1
            right = postorder(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return postorder(root) != -1
