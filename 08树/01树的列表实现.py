# 创建根节点
def BinaryTree(r):
    return [r, [], []]

# 插入左子树
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

# 插入右子树
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

# 树的访问函数
# 1.返回当前节点中存储的对象
def getRootVal(root):
    return root[0]

# 2.设置当前节点值
def setRootVal(root, newVal):
    root[0] = newVal

# 3.得到当前节点的左孩子
def getLeftChild(root):
    return root[1]

# 4.得到当前节点的右孩子
def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    insertLeft(r, 4)
    insertRight(r, 5)
    insertLeft(r, 6)
    insertRight(r, 7)
    print(r)