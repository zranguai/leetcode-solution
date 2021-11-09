# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
"""
# 标签:  滑动窗口 数学 双指针 枚举


# 解题思路:
"""
    两个指针 i, j = 1， 2  采用滑动窗口算法解决
    只要i < j
        如果和sum_value < target : j++
        如果和sum_value > target : i++
        如果和相等 记录值
    
"""


# 执行结果： 通过
"""
    执行用时：364 ms, 在所有 Python 提交中击败了9.14% 的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了63.05% 的用户
    通过测试用例：32 / 32
"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        i, j = 1, 2
        while i < j:
            sum_ = [index for index in range(i, j + 1)]
            sum_value = sum(sum_)
            if sum_value < target:
                j += 1
            elif sum_value > target:
                i += 1
            else:
                result.append(sum_)
                j += 1
        return result






if __name__ == '__main__':
    solution = Solution()
    target = 9
    res = solution.findContinuousSequence(target)
    # print(res)
