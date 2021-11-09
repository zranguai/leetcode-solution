# 一般冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:    # 大的先后面靠
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist


# 短冒泡排序
"""
    如果再一轮遍历中没有发生元素交换,就可以确定列表已经
    有序。可以修改冒泡排序算法，使其遇到这种情况提前终止
"""
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:  # 大的往后靠
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1
# 测试
if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # 正常冒泡排序
    # bS = bubbleSort(alist)
    # print(bS)

    # 短冒泡排序
    sBS = shortBubbleSort(alist)
    print(alist)