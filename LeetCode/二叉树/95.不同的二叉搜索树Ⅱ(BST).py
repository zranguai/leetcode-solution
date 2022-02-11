# 题目描述:
"""
    https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
"""
# 相关标签: 二叉搜索树 二叉树 树 动态规划 回溯

# 思路:
"""
    1. 穷举root节点的所有可能
    2. 递归构造出左右子树的所有合法BST
    3. 给root节点穷举所有左右子树的组合
    https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247490696&idx=1&sn=798a350fcca16c89572caf65323dbec7&ascene=7&devicetype=android-30&version=2800105d&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=A4UFp544CyEjOODfKintGME%3D&pass_ticket=dvgDix%2FYZvorZWUq8NPru7bMNh8A%2Fjbqc9mt7euH%2Bt02bMvfLWg21ti2hvhTpKNW&wx_header=3
"""

# 运行结果:
"""
    执行用时：36 ms, 在所有 Python 提交中击败了54.20%的用户
    内存消耗：16.7 MB, 在所有 Python 提交中击败了63.36%的用户
    通过测试用例：8 / 8
"""
# 方法1：


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    def build(self, lo, hi):
        res = []
        # base case
        if lo > hi:
            res.append(None)
            return res
        # 1. 穷举 root 节点的所有可能。
        for i in range(lo, hi + 1):
            # 2. 递归出左右子树的所有合法BST
            leftTree = self.build(lo, i - 1)
            rightTree = self.build(i + 1, hi)
            # 3. 给 root 节点穷举所有左右子树的组合。
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        # 构造闭区间 [1, n] 组成的 BST
        return self.build(1, n)


# 方法2：使用备忘录

# 运行结果:
"""
    执行用时：28 ms, 在所有 Python 提交中击败了92.37%的用户
    内存消耗：14.8 MB, 在所有 Python 提交中击败了99.62%的用户
    通过测试用例：8 / 8
"""


class Solution(object):
    def build(self, lo, hi, memo):
        res = []
        # base case
        if lo > hi:
            res.append(None)
            return res
        # 查备忘录
        if memo[lo][hi] != 0:
            # 如果res已经计算出来了，就直接返回
            return memo[lo][hi]

        # 1. 穷举 root 节点的所有可能。
        for i in range(lo, hi + 1):
            # 2. 递归出左右子树的所有合法BST
            leftTree = self.build(lo, i - 1, memo)
            rightTree = self.build(i + 1, hi, memo)
            # 3. 给 root 节点穷举所有左右子树的组合。
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        # 将结果存入备忘录
        memo[lo][hi] = res
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        # 备忘录初始化
        memo = [[0] * (n + 1) for _ in range(n + 1)]
        # 构造闭区间 [1, n] 组成的 BST
        return self.build(1, n, memo)


if __name__ == '__main__':
    pass
