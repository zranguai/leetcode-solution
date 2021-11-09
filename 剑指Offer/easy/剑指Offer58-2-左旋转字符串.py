# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""
# 标签: 数学 双指针 字符串


# 解题思路:
"""
    将前几个挑选出来放到后面来
"""

# 执行结果： 通过
"""
    执行用时：20 ms, 在所有 Python 提交中击败了51.17% 的用户
    内存消耗：13.8 MB, 在所有 Python 提交中击败了5.10% 的用户
    通过测试用例：34 / 34
"""



class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        res2 = list()
        j = 0
        while j < n:
            res2.append(s[j])
            j += 1
        res1 = [s[j] for j in range(j, len(s))]
        return "".join(res1 + res2)



if __name__ == '__main__':
    solution = Solution()
    s = "abcdefg"
    k = 2
    solution.reverseLeftWords(s, k)