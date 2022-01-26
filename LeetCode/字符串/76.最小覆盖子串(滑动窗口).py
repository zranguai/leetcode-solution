# 题目描述:
"""
    https://leetcode-cn.com/problems/minimum-window-substring/
"""
# 相关标签: 滑动窗口 字符串 哈希表

# 方法1：暴力法
# 思路:


"""
    根据两层for循环来判断s中最小覆盖t的子串
"""

# 运行结果:
"""

"""

import collections
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in range(len(s)):
            for j in range(len(s)):
                subS = s[i:j]
                # subS 包含t的所有字母:
                #     更新答案


# 方法2：滑动窗口法
# 思路:
"""
    https://labuladong.gitee.io/algo/2/21/58/
"""

# 运行结果: 通过
"""
    执行用时：112 ms, 在所有 Python 提交中击败了30.22%的用户
    内存消耗：13.4 MB, 在所有 Python 提交中击败了61.27%的用户
    通过测试用例：266 / 266
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        # valid表示窗口中满足条件的字符个数，若valid和need.size大小相同说明窗口已满足条件，完全覆盖t
        left, right, valid = 0, 0, 0
        # 记录最小覆盖子串的起始索引及长度
        start, length = 0, 1000
        while(right < len(s)):
            # c 是将移入窗口的字符
            c = s[right]
            right += 1
            # 进行window窗口内数据的一系列更新
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:  # 该子串要比上一个小才会更新
                    start = left
                    length = right - left
                # d 是将移出窗口的字符
                d = s[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 返回最小覆盖子串
        return "" if length == 1000 else s[start:start+length]



if __name__ == '__main__':
    solu = Solution()
    s = "ADOBECODEBANC"
    # s = "ADOBEC"
    t = "ABC"
    res = solu.minWindow(s, t)
    print(res)
