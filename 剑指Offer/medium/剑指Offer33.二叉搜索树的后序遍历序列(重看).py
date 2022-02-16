# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
"""
# 相关标签: 树 栈 二叉树 二叉搜索树 递归 单调栈
# 思路:
"""
    由数组构造二叉搜索树
"""
# 执行结果
"""
    执行用时：16 ms, 在所有 Python 提交中击败了78.39%的用户
    内存消耗：13.1 MB, 在所有 Python 提交中击败了66.76%的用户
    通过测试用例：23 / 23
"""


class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def recur(i, j):
            if i > j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1  # 找第一个比后面大的
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


