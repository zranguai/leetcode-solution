# 题目描述:
"""
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
# 相关标签: 滑动窗口 字符串 哈希表

# 思路:

"""
    采用滑动窗口解法
    当window没有重复字符时增加right
    当window出现重复时减小窗口
    当减小窗口的时候判断结果 res = max(res, right-left)
"""

# 运行结果: 通过
"""
    执行用时：52 ms, 在所有 Python 提交中击败了55.01%的用户
    内存消耗：13.4 MB, 在所有 Python 提交中击败了76.32%的用户
    通过测试用例：987 / 987
"""

import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = collections.defaultdict(int)
        left, right, res = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            # window[c]中有重复的时开始收缩窗口
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)  # 在这里更新答案
        return res


if __name__ == '__main__':
    solu = Solution()
    s = ""
    res = solu.lengthOfLongestSubstring(s)
    print(res)
