# 题目描述
"""
    https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
"""
# 标签: 树， 广度优先搜索
# 解题思路
"""
    相当于二叉树的层次遍历(使用队列辅助)
"""
# 执行结果
"""
    执行用时：8 ms, 在所有 Python 提交中击败了99.68%的用户
    内存消耗：13.3 MB, 在所有 Python 提交中击败了48.05%的用户
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []  # 空二叉树
        result = []
        queue = []
        queue.append(root)  # 根节点先入队列
        while queue:
            tmp = []
            for _ in range(len(queue)):  # 在这个循环里面-->队列中的都是同一层的
                node = queue.pop(0)
                tmp.append(node.val)

                # 为下一层做准备，将下一层的节点放进队列中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(tmp)
        return result


if __name__ == '__main__':
    solution = Solution()
    root = None
    solution.levelOrder(root)