# 2024-7-23 v0.1
# https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked
# tag:哈希

class Solution(object):
    def twoSum(self, nums, target):
        """
        使用hash表将时间复杂度将为O(n)  hashdict = dict()
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashdict = dict()  # 键为num, 值为num_idx
        for num_idx, num in enumerate(nums):
            hash_key = target - num
            if hash_key in hashdict.keys():  # 值在hash字典中，[hash字典的值为前一个目标的idx(提前存起来), 匹配的值idx]
                return [hashdict[hash_key], num_idx]
            else:
                hashdict[num] = num_idx  # 提前把值和对应的idx存起来
        return [] 
