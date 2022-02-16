# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
"""
# 相关标签: 树 数组 二叉树 哈希表 分治
# 思路:
"""
    从先序遍历找根节点，从中序遍历找左右节点
"""
# 执行结果
"""
    执行用时：100 ms, 在所有 Python 提交中击败了35.51%的用户
    内存消耗：22.2 MB, 在所有 Python 提交中击败了89.01%的用户
    通过测试用例：48 / 48
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(preorder, preStart, preEnd,
                  inorder, inStart, inEnd):
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            index = 0
            for i in range(inStart, inEnd + 1):  # 最后一个也要考虑上
                if inorder[i] == rootVal:
                    index = i
                    break
            leftSize = index - inStart
            root = TreeNode(rootVal)
            root.left = build(preorder, preStart + 1, preStart + leftSize,
                              inorder, inStart, index - 1)
            root.right = build(preorder, preStart + leftSize + 1, preEnd,
                               inorder, index + 1, inEnd)
            return root

        return build(preorder, 0, len(preorder) - 1,
                     inorder, 0, len(inorder) - 1)


if __name__ == '__main__':
    pass
