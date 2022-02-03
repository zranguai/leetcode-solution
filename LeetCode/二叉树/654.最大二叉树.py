# 题目描述:
"""
    https://leetcode-cn.com/problems/maximum-binary-tree/
"""
# 相关标签: 二叉树 栈 数组 分治 单调栈 树

# 思路:
"""
    1. 找到数组中最大值和最大值的索引作为根
    2. 左子树为最大值索引左边
    3. 右子树为最大值索引右边
"""

# 运行结果:
"""
    执行用时：96 ms, 在所有 Python 提交中击败了59.09%的用户
    内存消耗：13.7 MB, 在所有 Python 提交中击败了51.36%的用户
    通过测试用例：107 / 107
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def build(self, nums, start, end):
        # base case
        if start > end:
            return None
        index, maxVal = -1, -1
        for i in range(start, end+1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]
        root = TreeNode(maxVal)
        root.left = self.build(nums, start, index - 1)
        root.right = self.build(nums, index + 1, end)
        return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(max(nums))
    print(nums.index(max(nums)))
