# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
"""
# 标签: 数组 排序


# 解题思路:
"""
     1. 先将这5个数进行排序
     2. 根据0的个数来判断非0部分能够空几个格
"""

# 执行结果： 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了75.93% 的用户
    内存消耗：12.9 MB, 在所有 Python 提交中击败了90.61% 的用户
    通过测试用例：203 / 203    
"""


class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        # 统计0的个数
        sum0 = 0
        for i, value in enumerate(nums):
            if value == 0:
                sum0 += 1
            else:
                break
        # 使用两个指针，判断前后两个是否间隔大于sum0
        j = i + 1
        while j < len(nums):
            if nums[j] - nums[i] > sum0 + 1 or nums[j] == nums[i]:  # ***这里刚开始没有考虑到两张牌相等的情况
                return False
            else:
                i += 1
                j += 1
        return True
        # print(i, value, sum0)



if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0, 2, 2, 5]
    res = solution.isStraight(nums)
    print(res)
    # print(len(nums))
