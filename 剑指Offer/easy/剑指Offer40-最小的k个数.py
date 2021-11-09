# 题目描述
"""
    https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
"""
# 相关标签: 堆 分治算法
# 解题思路
"""
    1. 先使用快排使该列表有序 (从小到大排序)
    2. 取出前k小的数
"""
# 执行结果
"""
    执行用时：224 ms, 在所有 Python 提交中击败了20.72%的用户
    内存消耗：14.1 MB, 在所有 Python 提交中击败了76.48%的用户
"""


# 解法1：使用快排
class Solution1(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        def quickSort(arr, l, r):
            if l >= r: return
            i, j = l, r
            while i < j:
                temp = arr[l]
                while i < j and arr[j] >= temp: j -= 1  # 比temp小的
                while i < j and arr[i] <= temp: i += 1
                arr[i], arr[j] = arr[j], arr[i]  # 暂时交换i, j里面的值 --> 为了将arr[l]的值放到属于他的位置上
            arr[l], arr[i] = arr[i], arr[l]  # 最后将l的值属于他的位置，左右两边分号了

            quickSort(arr, l, i - 1)
            quickSort(arr, i + 1, r)

        quickSort(arr, 0, len(arr) - 1)
        print(arr[:k])  # 排好序了



# 解法2: 方法2: 堆
# 优先队列让你能够以任意顺序添加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。相比于列表方法min，这样做的效率要高得多。
class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return list()
        import heapq
        hp = [-x for x in arr[:k]]  # [-4, -5, -1, -6]
        heapq.heapify(hp)  # Transform list into a heap
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:  # 第一个元素永远是最小的  下面两句话相当于交换了堆里面的最大值与第i个值
                heapq.heappop(hp)  # Pop the smallest item off the heap
                heapq.heappush(hp, -arr[i])  # Push item onto heap
        ans = [-x for x in hp]
        return ans

# if __name__ == '__main__':
#     solu = Solution()
#     arr = [4, 5, 1, 6, 2, 7, 3, 8]
#     k = 4
#     res = solu.getLeastNumbers(arr, k)
#     print(res)



# 练习: 找出一列数组中最大的3个值
def findMax(arr):
    import heapq
    hp = [x for x in arr[:3]]
    heapq.heapify(hp)  # [1, 4, 5]

    for i in range(3, len(arr)):
        if i > hp[0]:
            heapq.heappop(hp)
            heapq.heappush(hp, arr[i])

    print(hp)





arr = [4, 5, 1, 6, 2, 7, 3, 8]
findMax(arr)



















