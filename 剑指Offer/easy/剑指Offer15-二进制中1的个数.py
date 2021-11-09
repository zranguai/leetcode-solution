# 题目描述  难度：简单
"""
https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
"""
# 相关标签： 位运算
# 思路：
"""
    使用位运算进行
"""
# 执行结果:
"""
执行用时：16 ms, 在所有 Python 提交中击败了80.99%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了65.05%的用户
"""
# 补充: python中>> << 都是位运算
# << 是左移末位补0类比十进制原数×10
# >> 是右移，相当于除以2



class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # n & 1相当于判断二进制的末尾是不是1---> 等同于 n % 2(取余)
            n >>= 1  # 相当于除以2
        return count

# 测试:
if __name__ == '__main__':

    solution = Solution()
    # n = 11111111111111111111111111111101
    n = 11  # 00000000000000000000000000001011
    # result = solution.hammingWeight(n)
    # print(result)
