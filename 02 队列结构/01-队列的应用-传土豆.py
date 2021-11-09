from Queue import Queue
"""
题目描述:n个人做成一个圆圈，每人一次喊数，喊道这个数的人出局，最后剩下live个人
"""

def hotPotato(namelist, num, live):
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)
    while queue.size() > live:
        for index in range(num):
            queue.enqueue(queue.dequeue())  # 进去后再出来
        queue.dequeue()  # 每循环num次就出来一个人
    return queue.items


potato = hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 6, 2)
print(potato)  # 这是最后存活下来的







