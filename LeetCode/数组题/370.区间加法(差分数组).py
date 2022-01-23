# 差分数组工具类
class Difference(object):
    def __init__(self):
        self.diff = []

    # 输入一个初始数组，区间操作将在这个数组上进行
    def difference(self, nums):
        assert len(nums) > 0
        m = len(nums)
        # 根据初始条件构造差分数组
        self.diff = [0] * (m+1)  # 创建和nums长度一致的全0数组
        nums.insert(0, 0)  # 往前面的数组增加一个0元素，方便后续操作
        for i in range(m + 1):
            self.diff[i] = nums[i] - nums[i - 1]
        nums.pop(0)
        self.diff.pop(0)

    # 给闭区间 [i,j] 增加 val（可以是负数）
    def increment(self, i, j, val):
        self.diff[i] += val  # i位置+val
        if j + 1 < len(self.diff):  # j位置-val,因为后续根据diff复原时后面重复加了
            self.diff[j+1] -= val
        print(self.diff)
    # 根据差分数组改变结果
    # 返回结果数组
    def result(self, nums):
        # res = [0] * len(self.diff)
        # res = nums
        res = self.diff  # bug1: 这里改成self.diff，如果是self.nums刚开始位置变化有无
        # 根据差分结果构造结果数组
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res  # ??
        # print(res)


# 区间加法
# 题目描述:
"""
    https://labuladong.gitee.io/algo/2/21/56/
"""
# 相关标签: 差分数组

# 思路:
"""
    根据上面提供的差分数组工具类，没进行一次操作后
    更新一次差分数组并且更新一次num值
"""

# 运行结果:
"""
   
"""

def getModifiedArray(length, updates):
    nums = [0] * length
    diff = Difference()
    for update in updates:
        i, j, val = update[0], update[1], update[2]
        diff.difference(nums)
        diff.increment(i, j, val)
        nums = diff.result(nums)
        print(nums)


if __name__ == '__main__':
    # test 差分数组工具类
    # diff = Difference()
    # nums = [8, 2, 6, 3, 1]
    # i, j, val = 1, 3, 3
    # diff.difference(nums)
    # diff.increment(i, j, val)
    # diff.result(nums)

    # test getModifiedArray
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    getModifiedArray(length, updates)








