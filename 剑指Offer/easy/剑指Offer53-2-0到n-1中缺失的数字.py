# -*-coding:utf-8-*-
 # 题目描述
"""
    https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
"""
# 标签: 位运算 数组 哈希表 数学 二分查找


# 解题思路:
"""
    使用两个数组进行对比
"""

# 执行结果： 通过
"""
执行用时：1068 ms, 在所有 Python 提交中击败了5.04% 的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了97.63% 的用户
通过测试用例：122 / 122
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    solution.missingNumber(nums)