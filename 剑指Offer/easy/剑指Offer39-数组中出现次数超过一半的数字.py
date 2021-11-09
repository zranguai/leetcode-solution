# 题目描述
"""
    https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
"""
# 相关标签: 位运算 分治算法
# 思路:
"""
    简单思路: 数组排序，找nums[len(nums) / 2]
"""
# 执行结果:
"""
    执行用时：32ms, 在所有 Python 提交中击败了65.26%的用户
    内存消耗：14.1 MB, 在所有 Python 提交中击败了32.95%的用户
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[int(len(nums) / 2)]

# if __name__ == '__main__':
#     solution = Solution()
#     # nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
#     nums = [1]
#     # res = solution.majorityElement(nums)
#     print(int(len(nums) // 2))
#
#     # print(res)



# 方法2: 投票法
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        for i in nums:
            if vote == 0: x = i






if __name__ == '__main__':
    solution = Solution2()
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution.majorityElement(nums)