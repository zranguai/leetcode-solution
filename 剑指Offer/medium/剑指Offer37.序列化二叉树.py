# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
"""
# 相关标签: 树 栈 二叉树 深度优先搜索 链表 双向链表
# 思路:
"""
    同leetcode297

"""
# 执行结果
"""
    执行用时：936 ms, 在所有 Python 提交中击败了5.30%的用户
    内存消耗：22.6 MB, 在所有 Python 提交中击败了94.71%的用户
    通过测试用例：48 / 48
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.res = ""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.serialize_(root)
        # print(self.res)
        # 列表变字符串
        return self.res

    def serialize_(self, root):
        if root == None:
            temp = "#" + ","
            self.res += temp
            return
        # 前序遍历位置
        ttemp = str(root.val) + ","
        self.res += ttemp
        self.serialize_(root.left)
        self.serialize_(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 将字符串转换为列表
        deress = data.split(",")
        deress.pop()
        return self.deserialize_(deress)

    def deserialize_(self, nodes):
        if len(nodes) == 0:
            return None
        # 列表最左侧就是根节点
        # print(nodes)
        first = nodes.pop(0)
        if first == "#": return None
        # first = int(first)
        root = TreeNode(first)
        root.left = self.deserialize_(nodes)
        root.right = self.deserialize_(nodes)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    pass
