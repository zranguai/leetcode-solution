# 题目描述
"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""
# 相关标签: 二分查找
# 思路:
"""
    使用二分查找策略:(因为数组是部分有序)
    使用first, last, mid：
        如果中间的值大于last值说明还在大的部分-->first往后移动
        如果中间的值小于last的值-->last往前移动
        否则last减少一个
"""
# 执行结果:
"""
执行用时：16 ms, 在所有 Python 提交中击败了86.97%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了40.64%的用户
"""


class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        first = 0
        last = len(numbers) - 1
        while first < last:
            mid = (first + last) // 2
            if numbers[mid] > numbers[last]:
                first = mid + 1
            elif numbers[mid] < numbers[last]:
                last = mid
            else:
                last -= 1
        return numbers[first]

# 测试
if __name__ == '__main__':
    solution = Solution()
    numbers = [3, 4, 5, 1, 2]
    result = solution.minArray(numbers)
    print(result)

