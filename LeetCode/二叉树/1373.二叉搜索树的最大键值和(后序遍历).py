# 题目描述:
"""
    https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/
"""
# 相关标签: 深度优先搜索 二叉搜索树 二叉树 树 动态规划

# 思路:
"""
    1、左右子树是否是 BST。
    2、左子树的最大值和右子树的最小值。
    3、左右子树的节点值之和。
    
    traverse(root) 返回一个大小为 4 的 int 数组，我们暂且称它为 res，其中：
    res[0] 记录以 root 为根的二叉树是否是 BST，若为 1 则说明是 BST，若为 0 则说明不是 BST；
    res[1] 记录以 root 为根的二叉树所有节点中的最小值；
    res[2] 记录以 root 为根的二叉树所有节点中的最大值；
    res[3] 记录以 root 为根的二叉树所有节点值之和。
"""

# 运行结果:
"""
    执行用时：380 ms, 在所有 Python 提交中击败了78.38%的用户
    内存消耗：60.7 MB, 在所有 Python 提交中击败了91.89%的用户
    通过测试用例：8 / 8
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = 0

    def traverse(self, root):
        if root == None:
            return [1, 100000, -100000, 0]
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        # 后序遍历位置
        res = [0, 0, 0, 0]
        # 判断以root为根的二叉树是不是 BST(左边是二叉树，右边是二叉树，根>左边 根<右边)
        if left[0] == 1 and right[0] == 1 and root.val > left[2] and root.val < right[1]:
            # 以 root 为根的二叉树是 BST
            res[0] = 1
            # 计算以 root 为根的这棵 BST 的最小值
            res[1] = min(left[1], root.val)
            # 计算以 root 为根的这棵 BST 的最大值
            res[2] = max(right[2], root.val)
            # 计算以 root 为根的这棵 BST 所有节点之和
            res[3] = left[3] + right[3] + root.val
            # 更新全局变量
            self.maxSum = max(self.maxSum, res[3])
        else:
            # 以 root 为根的二叉树不是 BST, 其他值不用计算
            res[0] = 0
        return res

    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.maxSum


if __name__ == '__main__':
    pass
