# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
"""
# 相关标签: 树 栈 二叉树 深度优先搜索 链表 双向链表
# 思路:
"""
    根据二叉搜索树的中序遍历是递增的特点
    
"""
# 执行结果
"""
    执行用时：36 ms, 在所有 Python 提交中击败了56.07%的用户
    内存消耗：13.8 MB, 在所有 Python 提交中击败了86.30%的用户
    通过测试用例：50 / 50
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(cur):
            if cur == None: return
            dfs(cur.left)  # 递归左子树
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                # 记录头节点
                self.head = cur
            self.pre = cur  # 保存cur
            dfs(cur.right)  # 递归右子树

        if root == None: return
        self.pre = None
        dfs(root)
        # 接上，首位相连
        self.head.left = self.pre
        self.pre.right = self.head

        return self.head


if __name__ == '__main__':
    pass
