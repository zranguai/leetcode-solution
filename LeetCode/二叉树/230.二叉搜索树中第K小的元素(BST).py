# 题目描述:
"""
    https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
"""
# 相关标签: 二叉搜索树 二叉树 树 深度优先搜索

# 思路:
"""
    1. 根据该树时二叉搜索树，二叉搜索树具有中序遍历时顺序是  从小到大
    2. 因此使用中序遍历得到第k大
"""

# 运行结果:
"""
    执行用时：48 ms, 在所有 Python 提交中击败了12.35%的用户
    内存消耗：20.7 MB, 在所有 Python 提交中击败了21.73%的用户
    通过测试用例：93 / 93
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = 0  # 记录结果
        self.rank = 0  # 记录当前排名

    def traverse(self, root, k):
        if root == None:
            return
        self.traverse(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return
        self.traverse(root.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.traverse(root, k)
        return self.res


if __name__ == '__main__':
    pass
