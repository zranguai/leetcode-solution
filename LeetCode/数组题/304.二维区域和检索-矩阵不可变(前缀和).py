# 题目描述:
"""
    https://leetcode-cn.com/problems/range-sum-query-2d-immutable/
"""
# 相关标签: 前缀和 数组 矩阵 设计

# 思路:
"""
    使用前缀和思想:
    具体参考: https://labuladong.gitee.io/algo/2/21/55/    
"""

# 运行结果: 通过
"""
   执行用时：2800 ms, 在所有 Python 提交中击败了38.26%的用户
   内存消耗：26.3 MB, 在所有 Python 提交中击败了18.79%的用户
   通过测试用例：24 / 24
"""
# 时间复杂度:
"""

"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        # self.preMatrix = [[0 for i_1 in range(len(self.matrix[0])+1)]] * (len(self.matrix) + 1)  # 这样做共享了内存，全部一样了
        self.preMatrix = [[0] * (n + 1) for _ in range(m + 1)]
        # print(self.preMatrix)
        for i in range(m):
            for j in range(n):
                self.preMatrix[i+1][j+1] = self.matrix[i][j] + self.preMatrix[i][j+1] + self.preMatrix[i+1][j] - self.preMatrix[i][j]
        # print(self.preMatrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        _sums = self.preMatrix
        return _sums[row2+1][col2+1] - _sums[row2+1][col1] - _sums[row1][col2+1] + _sums[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    pass