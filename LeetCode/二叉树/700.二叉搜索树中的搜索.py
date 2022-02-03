# 题目描述:
"""
    https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
"""
# 相关标签: 二叉搜索树 二叉树 树

# 思路:
"""
    还是根据二叉搜索树中序遍历出来的结果是从小到大的结论
    
"""

# 运行结果:
"""
    执行用时：52 ms, 在所有 Python 提交中击败了87.74%的用户
    内存消耗：16.9 MB, 在所有 Python 提交中击败了27.69%的用户
    通过测试用例：36 / 36
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
            # 找到了val返回节点
        return root


if __name__ == '__main__':
    pass
