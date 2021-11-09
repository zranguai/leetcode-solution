from Deque import Deque
"""
    检测一段字符串是不是回文
"""
def check_huiwen(str_huiwen):
    d = Deque()
    for i in str_huiwen:
        d.addRear(i)
    temp = True
    while d.size() > 1 and temp:
        rear = d.removeRear()
        front = d.removeFront()
        if rear != front:
            temp = False
    return temp


# 测试
check_huiwen = check_huiwen('rassar')
print(check_huiwen)


