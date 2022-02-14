# 题目描述:
"""
    https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""
# 相关标签: 深度优先搜索 二叉搜索树 二叉树 树 字符串

# 方法1：前序遍历
# 思路:
"""
    1. 序列化: 按照前序遍历将二叉树变成字符串
    2. 因为前序遍历带了空节点，所以复原时直接复原就行
"""

# 运行结果:
"""
    执行用时：916 ms, 在所有 Python 提交中击败了25.94%的用户
    内存消耗：22.7 MB, 在所有 Python 提交中击败了95.68%的用户
    通过测试用例：8 / 8
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
        # self.deres = []

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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


if __name__ == '__main__':
    # test
    # res = []
    # res.append(3)
    # print(res)
    deres = [3, 1, 2]
    rr = deres.pop()
    print(rr)
    print(deres)

    res = "1,2,#,#,3,4,#,#,5,#,#,"
    deres = res.split(",")
    # print(deres)
