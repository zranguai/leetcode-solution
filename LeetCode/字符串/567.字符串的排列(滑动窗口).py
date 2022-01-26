# 题目描述:
"""
    https://leetcode-cn.com/problems/permutation-in-string/
"""
# 相关标签: 滑动窗口 字符串 哈希表 双指针

# 思路:

"""
    1. 使用滑动窗口来进行解题
    与76题思路大概类似:
    在缩小窗口时，当left, right指针长度小于len(s1)时开始收缩
    当valid=s1.size时找到，返回True
"""

# 运行结果: 通过
"""
    执行用时：80 ms, 在所有 Python 提交中击败了34.06%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了88.28%的用户
    通过测试用例：106 / 106
"""

import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for i in s1:
            need[i] += 1
        left, right, valid = 0, 0, 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(need):  # 判断结束标志
                    return True
                d = s2[left]
                left += 1
                if d in need.keys():
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return False  # 未找到符合条件的子串


if __name__ == '__main__':
    solu = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    res = solu.checkInclusion(s1, s2)
    print(res)
