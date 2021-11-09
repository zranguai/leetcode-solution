from Stack import Stack

# 将10进制数转换成2进制数
def ten2two(number):
    s = Stack()
    while number > 0:
        rem = number % 2  # 余数
        div = number // 2  # 除数
        number = div
        s.push(rem)
    result = ''
    while not s.isEmpty():
        result += str(s.pop())
    return result


# 测试
# transform = ten2two(110)
# print(transform, type(transform))


#进阶--->将10进制转换成任意进制
def ten2anyone(number, anyone):
    s = Stack()
    while number > 0:
        rem = number % anyone  # 余数
        div = number // anyone  # 除数
        number = div
        s.push(rem)
    result = ''
    while not s.isEmpty():
        result += str(s.pop())
    return result

ttrans = ten2anyone(16, 8)
print(ttrans)
