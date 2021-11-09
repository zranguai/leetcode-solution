# -*-coding:utf-8-*-
 # 题目描述
"""
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
"""
# 标签: 树 深度优先搜索 二叉搜索树 二叉树

# 法一：
# 解题思路:
"""
    step1: 使用save_res数组进行存储
    
    step2: 采用 右 根 左 的遍历方式进行遍历存入数组，得到的是从大到小的数
    
    step3: 取出第k大节点
"""

# 执行结果： 通过
"""
执行用时：40 ms, 在所有 Python 提交中击败了47.78% 的用户
内存消耗：20.7 MB, 在所有 Python 提交中击败了16.12% 的用户
通过测试用例：91 / 91
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        save_res = []
        def dfs(root):
            if not root: return
            dfs(root.right)
            save_res.append(root.val)
            dfs(root.left)

        dfs(root)
        return save_res[k - 1]


# 法二:
# 解题思路
"""
    依次找出第二大的即可
"""
# 执行结果： 通过
"""
执行用时：52 ms, 在所有 Python 提交中击败了7.99% 的用户
内存消耗：20.7 MB, 在所有 Python 提交中击败了14.94% 的用户
通过测试用例：91 / 91
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if not root: return

            dfs(root.right)

            if self.k == 0: return

            self.k -= 1

            if self.k == 0: self.res = root.val

            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

if __name__ == '__main__':
    solution = Solution()

