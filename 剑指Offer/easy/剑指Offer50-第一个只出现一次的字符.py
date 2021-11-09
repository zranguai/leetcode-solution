# -*-coding:utf-8-*-
# 题目描述
"""
    https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""
# 标签: 队列 哈希表 字符串 计数


# 方法一
# 解题思路
"""
    使用两个队列: 一个是字符串s本身，例外一个是临时存储的队列temp，例外一个存储重复字符reuse
    step1： temp先出去一个，判断s[i]该元素是否还有在temp中的,如果其中还有就将s[i]存入reuse
    step2： 下次碰到在reuse的话，s和temp同时出队
"""

# 执行结果 : 超出时间限制
"""
    43 / 104 个通过测试用例
"""

class Solution01(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_ = list(s)
        import copy
        temp = copy.deepcopy(s_)
        s = copy.deepcopy(s_)
        reuse = []
        for i in s_:
            temp.pop(0)
            if i in temp:
                reuse.append(i)
                s.pop(0)
                continue
            elif i in reuse:
                s.pop(0)
            else:
                return i
        return ' '


# 方法二： 使用哈希表(字典方式)
# 解题思路
"""
    使用哈希表(字典来进行存储)
    step1:遍历一遍s,如果s中有重复的值将dic[i] = False
    step2: 依次遍历，找出第一个True的
"""

# 执行结果: 通过
"""
执行用时：64 ms, 在所有 Python 提交中击败了84.11% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了98.14% 的用户
通过测试用例：104 / 104
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = True
            else:
                dic[c] = False
        # 找出第一个不重复的
        for c in s:
            if dic[c] == True:
                return c
        return ' '


if __name__ == '__main__':
    solution = Solution()
    # s = "abaccdeff"
    s = ""
    res = solution.firstUniqChar(s)
    print(res)
