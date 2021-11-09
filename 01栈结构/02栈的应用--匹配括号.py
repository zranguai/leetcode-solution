from Stack import Stack

# 匹配简单的( )等
def parCheck(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced == True:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        else:
            pass
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


# # 测试部分
# pC = parCheck('((++(+)))')
# print(pC)


# 匹配更加复杂的括号({[]})等
def parCheck1(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced == True:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        else:
            pass
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# 代码改进---如果是这个情况会与预期不符pC1 = parCheck1('{+]()')--->为的是让(匹配),而不是(匹配]等
# 修改如下
def match(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
# 测试更加复炸的代码
pC1 = parCheck1('{+]()')
print(pC1)
