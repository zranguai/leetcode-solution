# 题目描述:
"""
    https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
# 相关标签: 二叉树 数组 树 哈希表 分治

# 思路:
"""
    根节点在后序遍历数组中，左右节点在中序遍历数组中
    1. 先在postorder[-1]找到根节点，然后在inorder中找到右子树 左子树 (先右后左)
    思路同105题
"""

# 运行结果:
"""
    执行用时：148 ms, 在所有 Python 提交中击败了22.77%的用户
    内存消耗：16.9 MB, 在所有 Python 提交中击败了96.86%的用户
    通过测试用例：202 / 202
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def build(self, inorder, inStart, inEnd,
              postorder, postStart, postEnd):
        if postStart > postEnd:
            return None
        index = 0
        rootVal = postorder[postEnd]
        for i in range(inStart, inEnd + 1):
            if inorder[i] == rootVal:
                index = i
                break
        rightSize = inEnd - index
        root = TreeNode(rootVal)
        # 先右后左
        root.right = self.build(inorder, index + 1, inEnd,
                                postorder, postEnd - rightSize, postEnd - 1)
        root.left = self.build(inorder, inStart, index - 1,
                               postorder, postStart, postEnd - rightSize - 1)
        return root

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, 0, len(inorder) - 1,
                          postorder, 0, len(postorder) - 1)


if __name__ == '__main__':
    pass
