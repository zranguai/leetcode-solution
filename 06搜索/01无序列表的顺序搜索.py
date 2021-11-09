# 无序列表的顺序搜索
def sequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

# 测试
if __name__ == '__main__':
    alist = [2, 5, 69, 58, 21, 69, 68]
    item = 22
    ss = sequentialSearch(alist, item)
    print(ss)
