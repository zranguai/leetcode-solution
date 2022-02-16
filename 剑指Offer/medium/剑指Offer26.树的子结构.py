# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/"""
# 相关标签: 树 深度优先搜索 二叉树
# 思路:
"""
    前序遍历 + 判断
    A中每出现一个值就进行判断(A, A.left, A.right)
    将A中的值和B里面进行比较
"""
# 执行结果
"""
    执行用时：100 ms, 在所有 Python 提交中击败了35.51%的用户
    内存消耗：22.2 MB, 在所有 Python 提交中击败了89.01%的用户
    通过测试用例：48 / 48
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        def recur(A, B):
            # B为空说明比完了
            if B == None: return True
            if A == None or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        # 1.A,B为空，2. A和B比较，3. A.left和B比较 4.A.right和B比较
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == '__main__':
    pass
