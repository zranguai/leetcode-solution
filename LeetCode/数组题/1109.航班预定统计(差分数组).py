# 差分数组工具类
class Difference(object):
    def __init__(self):
        self.diff = []

    # 输入一个初始数组，区间操作将在这个数组上进行
    def difference(self, nums):
        assert len(nums) > 0
        m = len(nums)
        # 根据初始条件构造差分数组
        self.diff = [0] * (m + 1)  # 创建和nums长度一致的全0数组
        nums.insert(0, 0)  # 往前面的数组增加一个0元素，方便后续操作
        for i in range(m + 1):
            self.diff[i] = nums[i] - nums[i - 1]
        nums.pop(0)
        self.diff.pop(0)

    # 给闭区间 [i,j] 增加 val（可以是负数）
    def increment(self, i, j, val):
        self.diff[i] += val  # i位置+val
        if j + 1 < len(self.diff):  # j位置-val,因为后续根据diff复原时后面重复加了
            self.diff[j + 1] -= val
        # print(self.diff)

    # 根据差分数组改变结果
    # 返回结果数组
    def result(self, nums):
        # res = [0] * len(self.diff)
        # res = nums
        res = self.diff  # bug1: 这里改成self.diff，如果是self.nums刚开始位置变化有无
        # 根据差分结果构造结果数组
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res  # ??
        # print(res)


# 题目描述:
"""
    https://leetcode-cn.com/problems/corporate-flight-bookings/
"""
# 相关标签: 差分数组 数组

# 方法1：
# 思路:
"""
    与370区间加法同
"""

# 运行结果: 超出时间限制？？？
"""
    46 / 63 个通过测试用例
"""


class Solution1(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * n
        diff = Difference()
        for booking in bookings:
            i, j, val = booking[0] - 1, booking[1] - 1, booking[2]
            diff.difference(nums)  # 构造差分数组
            diff.increment(i, j, val)  # 差分数组增加值
            nums = diff.result(nums)  # 根据差分数组还原出结果
        return nums
        # print(nums)

# 方法2：
# 思路:
"""
    差分数组
"""

# 运行结果:
"""
    执行用时：116 ms, 在所有 Python 提交中击败了20.48%的用户
    内存消耗：22.8 MB, 在所有 Python 提交中击败了60.24%的用户
    通过测试用例：63 / 63
"""


class Solution:
    def corpFlightBookings(self, bookings, n):
        nums = [0] * n
        for left, right, inc in bookings:  # 根据每个小值构造统一差分数组
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc

        for i in range(1, n):  # 根据差分数组还原
            nums[i] += nums[i - 1]

        return nums

if __name__ == '__main__':
    solu = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    solu.corpFlightBookings(bookings, n)


# 方法2
