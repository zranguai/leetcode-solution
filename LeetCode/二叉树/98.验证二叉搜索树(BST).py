# 题目描述:
"""
    https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
# 相关标签: 二叉搜索树 二叉树 树 深度优先搜索

# 思路:
"""
    https://labuladong.gitee.io/algo/2/18/26/
"""

# 运行结果:
"""
    执行用时：28 ms, 在所有 Python 提交中击败了77.50%的用户
    内存消耗：17.5 MB, 在所有 Python 提交中击败了66.95%的用户
    通过测试用例：80 / 80
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
    def isValidBST_(self, root, min, max):
        if root == None: return True

        if min != None and root.val <= min.val: return False
        if max != None and root.val >= max.val: return False

        return self.isValidBST_(root.left, min, root) and self.isValidBST_(root.right, root, max)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST_(root, None, None)


if __name__ == '__main__':
    pass
