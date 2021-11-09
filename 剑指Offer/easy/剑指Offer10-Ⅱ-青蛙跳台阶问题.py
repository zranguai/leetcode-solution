# 题目描述
"""
https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
"""
# 相关标签:递归
# 思路: 暴力法
"""
    1级台阶: 剩n-1个台阶 --> 有f(n-1)
    2级台阶: 剩n-2个台阶 --> 有f(n-2)
    
    所以: f(n) = f(n - 1) + f(n - 2)
"""
# 执行结果: 超出时间限制
"""
"""
# 暴力版
# class Solution(object):
#     def numWays(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 1
#         elif n == 1:
#             return 1
#         else:
#             return self.numWays(n - 1) + self.numWays(n - 2)


# 执行结果: 通过:
"""
执行用时：12 ms, 在所有 Python 提交中击败了92.62%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了58.28%的用户

"""
# 思路2: 动态规划版
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007

# 测试
if __name__ == '__main__':
    solution = Solution()
    n = 0
    result = solution.numWays(n)
    print(result)
