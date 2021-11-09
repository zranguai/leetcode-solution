# 有序列表的顺序搜索--->遇到没找到的就停止
# 默认列表的排序顺序是从小到大
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            stop = True
        else:
            pos = pos + 1
    return found


# 测试
if __name__ == '__main__':
    alist = [1, 3, 5, 6, 8, 9, 12, 55, 63]
    item = 11
    oss = orderedSequentialSearch(alist, item)
    print(oss)