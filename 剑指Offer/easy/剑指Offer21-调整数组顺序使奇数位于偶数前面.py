# 题目描述
"""
    https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""
# 相关标签: 数组
# 思路：
"""
    找两个指针，一个为start,一个为end
    start = 数组最开始。end = 数组最后面
    start向后面走(找偶数)，end向前面走(找奇数)。start碰到end时结束
    然后让他们两个交换
"""
# 执行结果: 通过
"""
    执行用时：40 ms, 在所有 Python 提交中击败了67.41%的用户
    内存消耗：18.3 MB, 在所有 Python 提交中击败了37.03%的用户
"""

class Solution(object):

    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] % 2 != 0:
                start += 1
            elif nums[end] % 2 == 0:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.exchange(nums)
    print(result)
