# 题目描述:
"""
    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
# 相关标签: 二叉树 数组 树 哈希表 分治

# 思路:
"""
    https://labuladong.gitee.io/algo/2/18/23/最后一个
"""

# 运行结果: 通过
"""
    执行用时：32 ms, 在所有 Python 提交中击败了29.27%的用户
    内存消耗：13 MB, 在所有 Python 提交中击败了75.61%的用户
    通过测试用例：306 / 306
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def build(self, preorder, preStart, preEnd,
                    postorder, postStart, postEnd):
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(preorder[preStart])
        rootVal = preorder[preStart]
        leftRootVal = preorder[preStart + 1]
        index = 0
        for i in range(postStart, postEnd):
            if postorder[i] == leftRootVal:
                index = i
                break
        leftSize = index - postStart + 1
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                               postorder, index + 1, postEnd - 1)
        return root

    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder) - 1,
                   postorder, 0, len(postorder) - 1)


if __name__ == '__main__':
    pass
