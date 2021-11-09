# -*-coding:utf-8-*-
# 题目描述 ***
"""
    https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/
"""
# 标签: 递归 数学 动态规划(???)


# 解题思路:
"""
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/si-bu-he-xin-gong-shi-qing-song-nong-don-3vln/     
"""

# 执行结果： 通过
"""
    执行用时：48 ms, 在所有 Python 提交中击败了52.13% 的用户
    内存消耗：16 MB, 在所有 Python 提交中击败了50.61% 的用户
    通过测试用例：36 / 36    
"""


class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        x = 0  # ????
        for i in range(2, n + 1):
            x = (x + m) % i
        return x


if __name__ == '__main__':
    solution = Solution()
    n = 10
    m = 17
    res = solution.lastRemaining(n, m)
    print(res)


