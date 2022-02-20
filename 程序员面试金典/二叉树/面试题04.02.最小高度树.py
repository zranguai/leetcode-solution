# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/minimum-height-tree-lcci/
"""
# 相关标签: 树 二叉搜索树 分治 二叉树
# 思路:
"""
    1. 根节点为数组的中心点
    2. 左子树为数组的左边
    3. 右子树为数组的右边
    设置时候build(nums, start, end), 注意边界条件
"""
# 执行结果
"""
    执行用时：24 ms, 在所有 Python 提交中击败了95.24%的用户
    内存消耗：17.5 MB, 在所有 Python 提交中击败了76.19%的用户
    通过测试用例：32 / 32
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(num, start, end):
            if start >= end:
                return None
            mid = start + (end - start) / 2
            midVal = num[mid]
            root = TreeNode(midVal)
            root.left = build(num, start, mid)
            root.right = build(num, mid + 1, end)
            return root

        return build(nums, 0, len(nums))


if __name__ == '__main__':
    pass
