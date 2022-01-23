# 题目描述:
"""
    https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
"""
# 相关标签: 左右双指针 链表

# 思路:
"""
    1. 使用左右双指针left=0 right=len(numbers) - 1
    2. 求出和target_temp = numbers[left] + numbers[right]
    3. 如果target_temp < target, left+1, 否则 right+1
    4. target_temp = target 返回 left+1 right+1
"""

# 运行结果: 通过
"""
    执行用时：20 ms, 在所有 Python 提交中击败了63.60%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了82.72%的用户
    通过测试用例：19 / 19
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1  # 左右双指针
        while left < right:
            target_temp = numbers[left] + numbers[right]
            if target_temp == target:
                return left + 1, right + 1  # 他是从1开始的
            elif target_temp < target:
                left += 1
            elif target_temp > target:
                right -= 1


if __name__ == '__main__':
    pass
