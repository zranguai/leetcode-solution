# -*-coding:utf-8-*-
# 题目描述 ***
"""
    https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
"""
# 标签: 位运算 数学

# 参考文章
"""
    https://www.runoob.com/w3cnote/bit-operation.html
    
    & 与 两个位都为1时结果才为1
    | 或 两个位结果为0时结果才为0
    ^ 异或 两个位相同为0 相异为1
    ~ 取反 0变1 1变0
    << 左移 高位丢弃 低位补0  左移一位相当于*2
    >> 右移 
"""

# 解题思路:  ????
"""

"""

# 执行结果：
"""
  执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
    内存消耗：35.1 MB, 在所有 Java 提交中击败了69.50% 的用户
    通过测试用例：51 / 51
"""


"""
class Solution {
    public int add(int a, int b) {
        while(b != 0) { // 当进位为 0 时跳出
            int c = (a & b) << 1;  // c = 进位
            a ^= b; // a = 非进位和
            b = c; // b = 进位
        }
        return a;
    }
}

"""

class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return


if __name__ == '__main__':
    solution = Solution()
    a = 1
    b = 4
    res = solution.add(a, b)
    print(res)

