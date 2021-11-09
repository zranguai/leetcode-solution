# 题目描述
"""
    https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
"""
# 相关标签: 数组
# 解题思路
"""
    设置好上下左右的边界，然后根据上下左右的边界考虑四种方向的情况
"""
# 执行结果
"""
    执行用时：16 ms, 在所有 Python 提交中击败了99.69%的用户
    内存消耗：13.7 MB, 在所有 Python 提交中击败了55.15%的用户
"""



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []: return []
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while True:
            for i in range(l, r+1):  # 从l --> r
                res.append(matrix[t][i])
            t += 1
            if t > b: break

            for i in range(t, b+1):  # 从t --> b
                res.append(matrix[i][r])
            r -= 1
            if l > r: break

            for i in range(r, l - 1, -1):  # 从r --> l    (要考虑到最后一个访问不到)
                res.append(matrix[b][i])
            b -= 1
            if t > b: break

            for i in range(b, t - 1, -1):  # 从b --> t
                res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res


if __name__ == '__main__':
    solution = Solution()
    matrix = []
    result = solution.spiralOrder(matrix)
    print(result)

