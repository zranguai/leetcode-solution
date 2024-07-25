# 2024-7-24 v0.1
# https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
# tag:哈希(set)  set中判断 for i in set(list)时间复杂度为O(1)


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlength = 0
        nums_set = set(nums)
        for num in nums:
            # 先确定该元素为该序列中最小的元素
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                while current_num + 1 in nums_set:  # 从该序列最小元素 从小往大选
                    current_num += 1
                    current_length += 1
                maxlength = max(current_length, maxlength)
        return maxlength


if __name__ == "__main__":
    solution = Solution()
    nums = [100,4,200,1,3,2]
    res_nums = solution.longestConsecutive(nums)
    print(res_nums)
