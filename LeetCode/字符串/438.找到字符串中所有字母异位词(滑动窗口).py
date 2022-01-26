# 题目描述:
"""
    https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
"""
# 相关标签: 滑动窗口 字符串 哈希表

# 思路:

"""
    与567字符串的排列思路同，唯一变的时将需要的索引加入到结果中
"""

# 运行结果: 通过
"""
    执行用时：116 ms, 在所有 Python 提交中击败了20.69%的用户
    内存消耗：14.1 MB, 在所有 Python 提交中击败了66.62%的用户
    通过测试用例：106 / 106
"""

import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for i in p:
            need[i] += 1
        left, right, valid = 0, 0, 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need.keys():
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        # return res
        print(res)
if __name__ == '__main__':
    solu = Solution()
    s = "baa"
    p = "aa"
    solu.findAnagrams(s, p)
