# 题目描述
"""
    https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
"""
# 标签: 分治算法，动态规划

# 法一: 使用滑动窗口
# 解题思路
"""
    step1: 使用滑动窗口(滑动窗口依次变大)
    step2: 窗口的大小从1开始到len(nums)
    step3: 注意边界条件
"""
# 执行结果
"""
    超出时间限制
    198 / 202 个通过测试用例
    状态：超出时间限制

"""

class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        save_last = []
        for i in range(0, len(nums)):

            max_value = -999
            first = 0
            last = i

            while last < len(nums):
                nums_sum = [nums[index] for index in range(first, last + 1)]
                if max_value < sum(nums_sum):
                    max_value = sum(nums_sum)
                first += 1
                last += 1
            save_last.append(max_value)

        # 打印出结果出来
        print(max(save_last))


# 法二：
# 解题思路
"""
    采用动态规划(难点在于这里的dp数组不好找)： 找出以nums[i]结尾的最大值, 主要根据dp[i-1]来进行判断
    初始状态: dp[0] = nums[0]
    递归方式:
        dp[i] = dp[i-1] + nums[i]   当dp[i-1]>0
        dp[i] = ums[i]   当dp[i-1]<0
"""

"""
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
dp   = [-2, 1, -2, 4, 3, 5, 6, 1, 5]
"""

# 运行结果: 通过
"""
执行用时：32 ms, 在所有 Python 提交中击败了92.45% 的用户
内存消耗：20.9 MB, 在所有 Python 提交中击败了13.05% 的用户
通过测试用例：202 / 202
"""

class Solution:
    def maxSubArray(self, nums):
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp.append(dp[i-1] + nums[i])
            else:
                dp.append(nums[i])
        print(max(dp))




if __name__ == '__main__':
    solu = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [1]
    solu.maxSubArray(nums)
    # nums_sub = [nums[i] for i in range(2) ]
    # print(sum(nums_sub))