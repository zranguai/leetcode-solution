# 题目描述： 难度: 中等
"""
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
"""
# 相关标签: 深度优先搜索
# 思路:
"""
https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
    使用深度优先搜索和剪纸操作---> 并用i,j分别代表行和列
    1. 如果 not (0<=i<len(board) or 0<=j<len(board[0]) or board[i][j]!=word[k]) return false
    2. k = len(word) - 1 return True
    3. 
"""
# 执行结果
"""
执行用时：192 ms, 在所有 Python 提交中击败了68.04%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了42.49%的用户
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''  # 将访问过的进行标记
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]  # 这个是将要访问的元素
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False



# 测试
if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = solution.exist(board, word)
    print(result)