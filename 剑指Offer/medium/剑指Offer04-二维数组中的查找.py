# 题目描述:
"""
    见leetcode官网链接:
    https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""
# 相关标签: 数组/双指针
# 思路:
"""
暴力搜索法:该方法不考虑每一行从左到右递增，不考虑从上到下递增
--->直接使用双重循环依次遍历解决
"""
# 执行结果:
"""
通过:执行用时：28 ms, 在所有 Python 提交中击败了65.43%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了84.31%的用户
"""


# # 法一:暴力法
# class Solution(object):
#     def findNumberIn2DArray(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         这里设置行为 line 列为 column
#         """
#         for line in range(len(matrix)):
#             if target in matrix[line]:
#                 return True
#         return False



# 法二:技巧版本:
"""
利用题目给的每一行从左到右递增顺序，每一列从上到下递增的顺序
这里先从矩阵的左下角开始搜索: 
    如果该值小于target就向右走一步，
    如果该值大于target就像上走一步
    如果找到了该值就返回True
    如果都没找到就返回False
"""
# 执行结果: 通过
"""
执行用时:36ms,在所有 Python 提交中击败了24.56%的用户
内存消耗：17.3 MB, 在所有 Python 提交中击败了15.48%的用户
"""

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        这里设置行为 line 列为 column
        """
        line = len(matrix) - 1  # 原始点在左下角
        column = 0
        while line >= 0 and column < len(matrix[0]):
            if matrix[line][column] > target:    # 向上寻找
                line -= 1
            elif matrix[line][column] < target:  # 向右寻找
                column += 1
            elif matrix[line][column] == target:  # 找到了
                return True
        return False



# 测试
if __name__ == '__main__':
    solution = Solution()
    matrix = \
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
    target = 100
    findNumberIn2DArray = solution.findNumberIn2DArray(matrix, target)
    print(findNumberIn2DArray)