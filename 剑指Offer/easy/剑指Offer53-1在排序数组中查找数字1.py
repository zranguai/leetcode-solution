 # 题目描述
"""
    https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""
# 标签: 数组 二分查找


# 解题思路:
"""
    二分查找， 使用两个指针，一个从前往后 一个从后往前
"""

# 执行结果： 通过
"""
    执行用时：20 ms, 在所有 Python 提交中击败了61.48% 的用户
    内存消耗：13.4 MB, 在所有 Python 提交中击败了26.58% 的用户
    通过测试用例：88 / 88
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        times = 0
        fast = 0
        last = len(nums)
        while fast < last:
            if nums[fast] < target:
                fast += 1
            elif nums[last - 1] > target:
                last -= 1
            else:
                times += 1
                fast += 1
        return times


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    solution.search(nums, target)

