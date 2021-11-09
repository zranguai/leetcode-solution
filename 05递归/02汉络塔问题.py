def moveDisk(fp, tp):
    print(f'move disk from {fp} to {tp}\n')


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)  # 可以理解成从A通过B移到C
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)  # 可以理解成从

moveTower(3, 'A', 'B', 'C' )  # 塔的高度是3，从A经过C移动到B

"""
       |
      |||
     |||||
--------------
      A
      
      |
      |
      |
--------------
      B
      
      |
      |
      |
--------------
      C
"""