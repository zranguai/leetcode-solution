# 1. 有序列表的二分搜索
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2  # 整除
        if alist[mid] == item:
            found = True
        else:
            if item > alist[mid]:
                first = mid + 1
            else:
                last = mid - 1
    return found


# 2. 二分搜索的递归写法
def digui_binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return digui_binarySearch(alist[:mid], item)
            else:
                return digui_binarySearch(alist[mid+1:], item)
# 测试
if __name__ == '__main__':
    alist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    item = 44
    digui_bS = digui_binarySearch(alist, item)
    print(digui_bS)
