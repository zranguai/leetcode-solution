# 题目描述:
"""
    https://leetcode-cn.com/problems/unique-binary-search-trees/
"""
# 相关标签: 二叉搜索树 二叉树 树 动态规划 数学

# 方法1：
# 思路:
"""
    # base case  
    if lo > hi: return 1
    
    # 所有的可能
    for i in range(lo, hi + 1):
        left = count(lo, i-1)
        right = count(i+1, hi)
        res += left*right
    return res
"""

# 运行结果: 超过时间限制
"""
    12 / 19 个通过测试用例
"""


class Solution1(object):
    def count(self, lo, hi):
        if lo > hi:
            return 1
        res = 0  # 把下一层的和进行置零
        for i in range(lo, hi + 1):
            left = self.count(lo, i - 1)
            right = self.count(i + 1, hi)
            res += left * right  # 累加和为左边和右边的乘积
        return res

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count(1, n)


# 方法2
# 运行结果: 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了62.56%的用户
    内存消耗：12.9 MB, 在所有 Python 提交中击败了91.78%的用户
    通过测试用例：19 / 19
"""
class Solution(object):
    def count(self, lo, hi, memo):
        if lo > hi:
            return 1
        # 查备忘录
        if memo[lo][hi] != 0:
            # 如果res已经计算出来了，就直接返回
            return memo[lo][hi]
        res = 0

        for i in range(lo, hi + 1):
            left = self.count(lo, i - 1, memo)
            right = self.count(i + 1, hi, memo)
            res += left * right
        # 将结果存入备忘录
        memo[lo][hi] = res
        return res

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 备忘录初始化
        memo = [[0] * (n + 1) for _ in range(n + 1)]
        return self.count(1, n, memo)


if __name__ == '__main__':
    pass
