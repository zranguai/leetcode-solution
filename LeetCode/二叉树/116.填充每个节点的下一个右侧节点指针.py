# 题目描述:
"""
    https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
"""
# 相关标签: 二叉树 深度优先搜索 广度优先搜索 树

# 思路:
"""
    如果只是使用一个节点，那么不能够连接夸父节点的两个相邻节点
    因此需要连接相同父节点的两个子节点和跨越父节点的两个子节点
"""

# 运行结果:
"""
    执行用时：212 ms, 在所有 Python 提交中击败了5.45%的用户
    内存消耗：15.9 MB, 在所有 Python 提交中击败了71.12%的用户
    通过测试用例：59 / 59
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connectTwoNode(self, node1, node2):
        if node1 == None or node2 == None:
            return
        node1.next = node2
        # 连接相同父节点的两个相邻节点
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)
        # 连接夸父节点的相邻节点
        self.connectTwoNode(node1.right, node2.left)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return
        self.connectTwoNode(root.left, root.right)
        return root


if __name__ == '__main__':
    pass
