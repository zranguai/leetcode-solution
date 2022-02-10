def traverse(arr, i):
    if (i == len(arr)):
        return
    # 前序遍历
    # print(arr[i])
    if i < 3:
        traverse(arr, i + 1)
    if i > 3:
        traverse(arr, i + 1)
    return i
    # traverse(arr, i + 1)
    # 后序遍历
    # print(arr[i])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    # i = 0
    print('start')
    res = traverse(arr, i=0)
    print(res)
    print("end")
