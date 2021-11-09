# 1.简单的循环来求和
def listSum(numList):
    theSum = 0
    for i in numList:
        theSum += i
    return theSum

# 2.使用递归来求和
# listSum(numList) = first(numList) + listSum(numList)
def listSum1(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum1(numList[1:])

# 3.将整数转换成以2-16进制基数的字符串
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]
# 测试
if __name__ == '__main__':
    numList = [1, 3, 5, 7, 9]
    # print(listSum(numList))
    # print(listSum1(numList))
    print(toStr(10, 2))