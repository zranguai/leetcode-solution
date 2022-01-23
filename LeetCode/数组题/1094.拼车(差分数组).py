# 题目描述:
"""
    https://leetcode-cn.com/problems/car-pooling/
"""
# 相关标签: 差分数组

# 思路:
"""
    # 该题整体思路同1109.航班预定统计
    1.因为整个站点长度不超过1000所以设计一个nums全0的数组长度为1001
    2.根据trips构造差分数组diff
    3.根据差分数组还原出原数组 如果大于capacity显示超载
"""

# 运行结果: 通过
"""
    执行用时：20 ms, 在所有 Python 提交中击败了78.48%的用户
    内存消耗：13.3 MB, 在所有 Python 提交中击败了63.29%的用户
    通过测试用例：59 / 59
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # 构造nums数组 题目给的提示最大站为1000
        nums = [0] * 1001
        # 构建差分数组
        for val, left, right in trips:
            if val > capacity:  # 一开始上车的人数就超载
                return False
            nums[left - 1] += val
            if right < 1001:
                nums[right-1] -= val  # 最后的情况不考虑

        # 根据差分数组还原
        for i in range(1, 1001):
            nums[i] += nums[i-1]
            if nums[i] > capacity:
                return False
        return True
        # print(nums)


if __name__ == '__main__':
    solu = Solution()
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 4

    trips = [[9, 0, 1], [3, 3, 7]]
    capacity = 4
    res = solu.carPooling(trips, capacity)
    print(res)

"""
[[53,318,446],[9,355,358],[45,543,585],[19,548,625],[65,572,624],[60,708,853],[77,125,651],[60,697,828],[100,28,199],[42,531,699],[40,536,641],[48,855,925],[100,746,992],[24,28,459],[54,108,812],[94,325,749],[32,200,348],[49,459,461],[96,429,750],[38,370,505],[86,49,184],[30,651,729],[2,225,547],[32,129,852],[100,238,949],[17,137,398],[95,431,870],[47,856,906],[74,511,721],[29,558,883]]
863
"""