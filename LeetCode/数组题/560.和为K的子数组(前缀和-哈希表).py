# 题目描述:
"""
    https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""
# 相关标签: 前缀和 数组 哈希表

# 方法1： 仅仅使用前缀和 超出时间限制
# 思路:
"""
    前提条件: 和为K的连续子数组与303题求i到j范围内元素的总和类似
    step1: 求出整数数组nums的前缀和preNums
    step2: 使得preNums的后面的元素减去前面的元素得到的结果为k时统计个数+1
"""

# 运行结果: 超出时间限制
"""
   通过测试用例：72/89
"""
#
"""
    时间复杂度: O(n^2)
    空间复杂度: O(n)
"""


class Solution1(object):
    def preSums(self, nums):
        m = len(nums)
        self.preSum = [0] * (len(nums)+1)
        # print(self.preSum)
        for i in range(m):
            self.preSum[i+1] = nums[i] + self.preSum[i]
        # print(self.preSum)
        return self.preSum

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSu = self.preSums(nums)
        n = len(preSu)
        res = 0
        # 使用双重循环解决 ---> 注意考虑边界条件
        # for i in range(n):
        #     for j in range(i, n):
        #         if preSu[j] - preSu[i] == k:
        #             res += 1

        # 使用双重循环解决
        for i in range(n-1):
            for j in range(i, n-1):
                if (preSu[j + 1] - preSu[i]) == k:
                    res += 1
        print(res)


# 方法二： 使用前缀和+HashMap
# 运行结果: 超出时间限制
"""
    执行用时：48 ms, 在所有 Python 提交中击败了87.04%的用户
    内存消耗：14.9 MB, 在所有 Python 提交中击败了91.36%的用户
    通过测试用例：89 / 89
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum_map = {0: 1}

        pre_sum = 0
        count = 0

        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_map:
                count += pre_sum_map[pre_sum-k]
            if pre_sum in pre_sum_map:
                pre_sum_map[pre_sum] += 1
            else:
                pre_sum_map[pre_sum] = 1
        return count
        # print(count)


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2, 1]
    k = 2
    solution.subarraySum(nums, k)

"""
总结:
前缀和主要适用的场景是原始数组不会被修改的情况下，频繁查询某个区间的累加和。
"""
