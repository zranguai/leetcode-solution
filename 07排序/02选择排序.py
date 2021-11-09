# 选择排序
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):  # 进行遍历-->将从大到小输出
        maxposition = 0
        for location in range(1, fillslot + 1):  # 在这一批次中找出最大的位置
            if alist[location] > alist[maxposition]:
                maxposition = location
        # 进行交换-->每次将最后面的值和前面最大的值进行交换
        temp = alist[fillslot]
        alist[fillslot] = alist[maxposition]
        alist[maxposition] = temp



# 测试
if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sS = selectionSort(alist)
    print(alist)