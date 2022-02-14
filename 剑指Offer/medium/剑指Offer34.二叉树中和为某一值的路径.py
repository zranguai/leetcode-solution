# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
"""
# 相关标签: 树 广度优先搜索 二叉树
# 思路:
"""
    1. 使用先序遍历的方式
    2. path记录到当前节点的路径，res保存结果
"""
# 执行结果
"""
    执行用时：24 ms, 在所有 Python 提交中击败了84.77%的用户
    内存消耗：15.4 MB, 在所有 Python 提交中击败了92.05%的用户
    通过测试用例：114 / 114
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        path, res = [], []

        def pathSum_(root, tar):
            if root == None:
                return
            # 采用先序遍历
            path.append(root.val)
            tar -= root.val
            # 到达根节点
            if tar == 0 and root.left == None and root.right == None:
                # print(path)
                res.append(list(path))
                # print(res)

            pathSum_(root.left, tar)
            pathSum_(root.right, tar)
            # 离开该节点
            path.pop()

        pathSum_(root, target)
        return res


if __name__ == '__main__':
    pass
