# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
"""
# 标签: 树 深度优先搜索 广度优先搜索 二叉树


# 解题思路:
"""
    这里使用层次遍历
    queue数组存储树节点  temp数组存储该节点下一层节点  然后用res统计结果
"""

# 执行结果： 通过
"""
执行用时：24 ms, 在所有 Python 提交中击败了80.39% 的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了32.88% 的用户
通过测试用例：39 / 39
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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





