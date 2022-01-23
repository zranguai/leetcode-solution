# 题目描述:
"""
    https://leetcode-cn.com/problems/reverse-string/
"""
# 相关标签: 左右双指针 字符串 递归

# 思路:
"""
    1. 使用左右双指针left=0 right=len(numbers) - 1
    2. 依次交换 s[left]和s[right]的值
"""

# 运行结果: 通过
"""
    执行用时：40 ms, 在所有 Python 提交中击败了33.76%的用户
    内存消耗：20.2 MB, 在所有 Python 提交中击败了79.96%的用户
    通过测试用例：477 / 477
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1  # 左右双指针
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    pass
