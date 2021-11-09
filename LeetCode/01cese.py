class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return list(set(nums))


if __name__ == '__main__':
    nums = [1,1,2, 3, 3, 5, 1]
    solu = Solution()
    res = solu.removeDuplicates(nums)
    print(res)