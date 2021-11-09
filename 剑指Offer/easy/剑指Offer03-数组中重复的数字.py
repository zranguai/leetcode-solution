# 题目描述:
"""
    见leetcode官网链接:
    https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""
# 相关标签: 数组/哈希表
# 思路:
"""
    依次遍历数组，看看前面的元素是否在后面出现过(用python中的in函数)
    从第一个元素开始,搜索的是第一个元素后面的列表(用python中的列表切片)
"""

# 运行结果:
"""
    22/24个通过测试用例
    状态:超出时间限制
"""
# 第一版:时间超出限制
#
# class Solution(object):
#     def findRepeatNumber(self, nums):
#         """
#         # :type nums: List[int]
#         # :rtype: int
#         """
#         index = 0
#         for i in nums:
#             target = i
#             if target in nums[index + 1:]:
#                 return target
#             else:
#                 index += 1


# 第二版
# 思路:
"""
    1.先排序
    2. 然后依次比较前后两个元素是否相等
"""
# 结果:
"""
执行结果：
通过
显示详情
执行用时：
16 ms
, 在所有 Python 提交中击败了
99.83%
的用户
内存消耗：
20.3 MB
, 在所有 Python 提交中击败了
32.62%
的用户
"""
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return nums[i]


# 测试
if __name__ == '__main__':
    solution = Solution()
    nums = [3, 5, 3, 0, 2, 5, 3]
    result = solution.findRepeatNumber(nums)
    print(result)