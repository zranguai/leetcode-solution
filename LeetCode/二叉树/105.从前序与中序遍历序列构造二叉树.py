# 题目描述:
"""
    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
# 相关标签: 二叉树 数组 树 哈希表 分治

# 思路:
"""
    根节点在先序遍历数组中，左右节点在中序遍历数组中
    先找到根节点，然后在inorder中找到根节点索引
"""

# 运行结果:
"""
    执行用时：144 ms, 在所有 Python 提交中击败了25.36%的用户
    内存消耗：17.6 MB, 在所有 Python 提交中击败了62.47%的用户
    通过测试用例：203 / 203
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def build(self, preorder, preStart, preEnd,
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
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                               inorder, index + 1, inEnd)
        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1)


if __name__ == '__main__':
    pass
