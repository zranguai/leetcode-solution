# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""
# 标签: 数组 双指针 二分查找


# 方法1
# 解题思路:
"""
    这里使用双指针
    第一个指针从前面开始(first), 第二个指针向后开始(last)
    第一个指针的值为nums[first], 第二个指针从后找值为target - nums[first]
    当第二个指针的和第一个重合后，first在向后移动一下
"""

# 执行结果： 超出时间限制
"""
    26 / 36 个通过测试用例
"""


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        first = 0
        last = len(nums) - 1

        while first < last:
            value1 = nums[first]
            value2 = target - value1
            result = [nums[i] for i in range(first + 1, last + 1)]
            if value2 in result:
                res.append(value1)
                res.append(value2)
                break
            first += 1
        return res



# 方法2
# 解题思路
"""
    使用两个指针 一前一后
    计算这两个指针的值
        如果小于target 前面指针后移
        如果大于target 后面指针前移
"""
# 执行结果
"""
    执行用时：72 ms, 在所有 Python 提交中击败了89.74% 的用户
    内存消耗：21.7 MB, 在所有 Python 提交中击败了29.71% 的用户
    通过测试用例：36 / 36
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i < j:
            value = nums[i] + nums[j]
            if value < target:
                i += 1
            elif value > target:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return []




if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    re= solution.twoSum(nums, target)
    print(re)
















