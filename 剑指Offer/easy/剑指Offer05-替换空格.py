# 题目描述
"""
    https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
"""
# 相关标签: 无
# 思路:
"""
    使用字符串的replace？？？--->第三个参数如果写就代表替换几个元素
"""
# 执行结果: 通过
"""
执行用时:24ms,在所有 Python 提交中击败了18.92%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了99.19%的用户
"""
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(' ', '%20')


# 测试
if __name__ == '__main__':
    solution = Solution()
    s = "We are happy."
    print(solution.replaceSpace(s))
