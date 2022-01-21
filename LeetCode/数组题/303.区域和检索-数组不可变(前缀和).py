# 题目描述:
"""
    见leetcode官网链接:
    https://leetcode-cn.com/problems/range-sum-query-immutable/
"""
# 相关标签: 前缀和 数组 设计

# 方法一: 直接计算
# 思路:
"""
    计算数组的某一个区间的值
"""

# 运行结果: 通过
"""
执行用时：496 ms, 在所有 Python 提交中击败了32.68%的用户
内存消耗：16.5 MB, 在所有 Python 提交中击败了90.16%的用户
通过测试用例：15 / 15    
"""
# 时间复杂度: O(N)
"""
N代表nums数组的长度
"""


class NumArray1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# 方法二: 使用前缀和法将时间复杂度降为O(1)
# 思路:
"""
    1. 提前准备个数组preSum
    2. 先将nums数组的前n项和存储在preSum中
    3. 取[0, 2]时直接从preSum中取 res = preSum(2+1) - preSum(0)
"""
# 执行结果：通过
"""
执行用时：152 ms, 在所有 Python 提交中击败了90.94%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了20.08%的用户
通过测试用例：15 / 15   
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.preSum = [0 for i in range(len(self.nums))]  # 构造全0的长度和nums相同
        for i, val in enumerate(self.nums):
            self.preSum[i] = self.preSum[i-1] + val  # 构造前缀和
        self.preSum.insert(0, 0)  # 往第一个前面添加0

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right + 1] - self.preSum[left]

if __name__ == '__main__':
    # nA = NumArray()
    # nums = [1, 3, 4, 5, 6]
    # print(sum(nums[1:3]))
    print(int[8])


# [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 3, 3, 4, 8, 10], [0, 8, 14, 18, 24, 27], [0, 9, 17, 21, 28, 36], [0, 13, 22, 26, 34, 49], [0, 14, 23, 30, 38, 58]]
