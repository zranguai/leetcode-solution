# -*-coding:utf-8-*-
# 题目描述 ***
"""
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""
# 标签: 树 深度优先搜索 二叉搜索树 二叉树

# 解题思路:
"""
    根据是二叉搜索树的条件来看，综合下面三种条件来看
    
    可能情形：
    1. p和q在root的子树中，且分别在root的两侧
    2. p=root, 且q在root的左或右子树
    3. q=root, 且p在root的左或右子树
"""

# 执行结果： 通过
"""
    执行用时：60 ms, 在所有 Python 提交中击败了28.99% 的用户
    内存消耗：21 MB, 在所有 Python 提交中击败了17.69% 的用户
    通过测试用例：27 / 27
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
        while root:
            if root.val < p.val and root.val < q.val:  # p and q 都在root左边
                root = root.right
            elif root.val > p.val and root.val > q.val:  # p and q 都在root左边
                root = root.left
            else:  # p and q 在root的两侧
                break
        return root

if __name__ == '__main__':
    solution = Solution()
    root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p = 2
    q = 8
    res = solution.lowestCommonAncestor(root, p, q)