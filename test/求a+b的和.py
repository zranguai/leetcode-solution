#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# 判断两个数组中的元素是否相等
def equ(lst1, lst2):
    for i in lst1:
        if i not in lst2:
            return False
    return True

def substr(str):
    # 先把字符串中有那些存下
    count = 0
    temp1 = []
    temp2 = []
    for i in str:
        if i not in temp1:
            temp1.append(i)

    for i in str:
        temp2.append(i)
        # 判断以a为起点的第一个包含所有元素的是不是最短的
        if equ(temp1, temp2):
            minstr = str(temp2)





# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
str = "abbbaaccb"
substr(str)
