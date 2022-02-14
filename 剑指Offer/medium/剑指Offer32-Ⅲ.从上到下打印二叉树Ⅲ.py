# 题目描述： 难度: 中等
"""
    https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
"""
# 相关标签: 树 广度优先搜索 二叉树
# 思路:
"""
    二叉树的层次遍历，使用collectin.deque
    根据再deque里面的都是在同一层的，然后各层添加方式不同
    奇数层append添加,偶数层insert(0, obj)添加
"""
# 执行结果
"""
    执行用时：16 ms, 在所有 Python 提交中击败了87.57%的用户
    内存消耗：13.4 MB, 在所有 Python 提交中击败了67.57%的用户
    通过测试用例：34 / 34
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
        import collections
        if root == None:
            return []
        res, dequeue = [], collections.deque()
        dequeue.append(root)
        flag = False  # 记录层数是双层(->1)还是单层(->0)
        while dequeue:
            tmp = []
            # 在这个循环里面 -->队列中的都是同一层的
            for _ in range(len(dequeue)):
                node = dequeue.popleft()
                if flag == False:
                    tmp.append(node.val)
                if flag == True:
                    tmp.insert(0, node.val)
                # 为下一层做准备，将下一层的节点放进队列中
                if node.left:
                    dequeue.append(node.left)
                if node.right:
                    dequeue.append(node.right)
            res.append(tmp)
            flag = not flag
        return res


if __name__ == '__main__':
    # test
    tmp = [1, 2, 3]
    tmp.insert(0, 4)
    print(tmp)
    flag = 1
    flag = not flag
    print(flag)
