# 题目描述:
"""
    https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
"""
# 相关标签: 数学
# 思路:
"""
    利用1位数的话是10**1 - 1
    二位数的话是10**2 - 1
    三位数的话是10**3 - 1
    然后进行遍历存进list即可
"""
# 执行结果
"""
    执行用时：28 ms, 在所有 Python 提交中击败了83.43%的用户
    内存消耗：25.1 MB, 在所有 Python 提交中击败了5.04%的用户
"""


class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        temp = 10**n -1
        res = []
        for i in range(temp):
            res.append(i + 1)
        return res



# 测试
if __name__ == '__main__':
    solution = Solution()
    n = 1
    result = solution.printNumbers(n)
    print(result)













