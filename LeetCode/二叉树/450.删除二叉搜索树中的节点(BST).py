# 题目描述:
"""
    https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
"""
# 相关标签: 二叉搜索树 二叉树 树

# 思路:
"""
    情况1：A恰好是末端节点，两个子节点都为空，直接删除
    情况2：A只有一个非空子节点，让他的儿子节点接替他
    这两种情况可合为：
        if root.left == None: return root.right
        if root.right == None: return root.left
    情况3：A有两个子节点，为了不破坏BST性质，找右子树最大的那个节点接替自己
        1. 找右子树最小的节点 getMin(root.right)
        2. 删除最小的节点 deleteNode(root.right, minNode.val)
        3.  minNode.left = root.left
            minNode.right = root.right
            root = minNode
"""

# 运行结果:
"""
    执行用时：56 ms, 在所有 Python 提交中击败了43.78%的用户
    内存消耗：21.1 MB, 在所有 Python 提交中击败了6.03%的用户
    通过测试用例：36 / 36
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMin(self, root):
        while root.left != None: root = root.left
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.val == key:
            # 情况1，情况2
            if root.left == None: return root.right
            if root.right == None: return root.left
            # 情况3
            minNode = self.getMin(root.right)  # 找到
            root.right = self.deleteNode(root.right, minNode.val)  # 删除
            minNode.left = root.left  # 替换
            minNode.right = root.right
            root = minNode

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        return root


if __name__ == '__main__':
    pass
