# 题目描述:
"""
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
# 相关标签: 深度优先搜索 二叉树 树

# 思路:
"""
    https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485561&idx=1&sn=a394ba978283819da1eb34a256f6915b&ascene=15&devicetype=android-30&version=28001339&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=AxiDoo6abod%2FaMF%2Bj6DjV5U%3D&pass_ticket=HE7fn%2FpStGGB3iZrBly5Gwml9B%2B9qYHb%2BPbO0GTFtBbhG3aZ%2FawGipxrhpy0Rt8%2F&wx_header=3
"""

# 运行结果:
"""
    执行用时：44 ms, 在所有 Python 提交中击败了93.28%的用户
    内存消耗：24.6 MB, 在所有 Python 提交中击败了88.96%的用户
    通过测试用例：31 / 31
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        if root == p or root == q: return root

        # 采用后序遍历
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 情况1: p和q都在以root为根的树中
        if left and right:
            return root
        # p和q都不在以root为根的树中
        elif left == None and right == None:
            return None
        # p和q其中一个在以root为根的树中
        return left if left else right


if __name__ == '__main__':
    pass
