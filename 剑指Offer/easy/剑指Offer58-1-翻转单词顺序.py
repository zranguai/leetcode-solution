# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
"""
# 标签: 双指针 字符串


# 解题思路:
"""
    通过字符串的方法操作
"""

# 执行结果： 通过
"""
    执行用时：16 ms, 在所有 Python 提交中击败了83.82% 的用户
    内存消耗：13.9 MB, 在所有 Python 提交中击败了86.41% 的用户
    通过测试用例：25 / 25  
"""



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        s = [st for st in s if st != '']
        s.reverse()
        return ' '.join(s)


if __name__ == '__main__':
    solution = Solution()
    s = " the  sky is blue! "
    res = solution.reverseWords(s)
    # print(res)