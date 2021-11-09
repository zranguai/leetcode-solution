# 题目描述
"""
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
"""
# 相关标签：递归，动态规划
# 思路1：
"""
    暴力求解法: 直接使用递归实现
"""
# 执行结果: 超出时间限制
"""
超出时间限制
"""


# 思路1：暴力法:
# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)


# 思路2: 动态规划版--->注意其中的状态转移方程
# 执行结果:通过
"""
执行用时：16 ms, 在所有 Python 提交中击败了75.99%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了47.78%的用户

"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b  # 这个为Fibonacci的状态转移方程
        return a % 1000000007  # 疑问???为什么要取余 --> 小于该数取本身
# 1000000007
# 测试:
if __name__ == '__main__':
    solution = Solution()
    n = 2
    ret = solution.fib(n)
    print(ret)


