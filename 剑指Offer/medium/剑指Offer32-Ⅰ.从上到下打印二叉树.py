# 题目描述： 难度: 中等
"""
https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
"""
# 相关标签: 树 广度优先搜索 二叉树
# 思路:
"""
    二叉树的层次遍历，使用collectin.deque
"""
# 执行结果
"""
    执行用时：20 ms, 在所有 Python 提交中击败了59.17%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了99.67%的用户
    通过测试用例：34 / 34
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        if root == None:
            return []
        res, deque = [], collections.deque()
        deque.append(root)
        while deque:
            node = deque.popleft()
            res.append(node)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res


if __name__ == '__main__':
    pass
