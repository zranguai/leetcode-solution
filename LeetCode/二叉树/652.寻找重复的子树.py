# 题目描述:
"""
    https://leetcode-cn.com/problems/find-duplicate-subtrees/
"""
# 相关标签: 二叉树 数组 树 哈希表 分治

# 思路:
"""
    序列化二叉树
"""

# 运行结果: 通过
"""
    执行用时：64 ms, 在所有 Python 提交中击败了13.68%的用户
    内存消耗：25.8 MB, 在所有 Python 提交中击败了9.48%的用户
    通过测试用例：176 / 176
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        import collections
        count = collections.Counter()
        res = []

        def collect(node):
            if not node: return "#"
            serial = "{}, {}, {}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                res.append(node)
            return serial
        collect(root)
        return res


if __name__ == '__main__':
    pass
