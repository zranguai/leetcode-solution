# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/check-subtree-lcci/
"""
# 相关标签: 树 深度优先搜索 字符串匹配 哈希函数 二叉树

# 方法1
# 思路:
"""
    1. 将T2的前序遍历用字符串表示出来serial
    
    2. 在T1的前序遍历中判断T2是否是T1的子树 
"""
# 执行结果
"""
    执行用时：148 ms, 在所有 Python 提交中击败了6.7%的用户
    内存消耗：31.3 MB, 在所有 Python 提交中击败了6.7%的用户
    通过测试用例：32 / 32
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkSubTree(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        import collections
        hashMap = collections.Counter()

        def T2(node):
            if node == None:
                return "#"
            serial = "{}, {}, {}".format(node.val, T2(node.left), T2(node.right))
            return serial

        seri = T2(t2)
        hashMap[seri] = 1

        # print(seri)
        def T1(node):
            if node == None:
                return "#"
            serial = "{}, {}, {}".format(node.val, T1(node.left), T1(node.right))
            hashMap[serial] += 1
            return serial

        T1(t1)
        if hashMap[seri] >= 2:
            return True
        else:
            return False


# 方法2：
# 思路:
"""
    将T2表示为字符串
    然后去T1中寻找
"""

# 运行结果: 通过
"""
    执行用时：92 ms, 在所有 Python 提交中击败了36.67%的用户
    内存消耗：28.8 MB, 在所有 Python 提交中击败了23.33%的用户
    通过测试用例：176 / 176
"""


class Solution(object):
    def checkSubTree(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        if t1 == None:
            return not t2  # t1为空时，t2也为空是返回True
        if t2 == None:
            return True
        return self.sameTree(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def sameTree(self, t1, t2):
        # 当t2为空是表示二者相等
        if t2 == None:
            return True
        if t1.val != t2.val or (t1 != None and t2 == None):
            return False
        return self.sameTree(t1.left, t2.left) and self.sameTree(t1.right, t2.right)


if __name__ == '__main__':
    pass
