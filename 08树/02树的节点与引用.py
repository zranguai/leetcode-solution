# 树的节点与引用
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # 1.插入左子节点
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:    # 插入一个节点，并将已有的左子节点降一层
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    # 1.插入右子节点
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:    # 插入一个节点，并将已有的左子节点降一层
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # 二叉树的访问函数
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # 二叉树的遍历

    # 1.前序遍历
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    # 2. 中序遍历
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    # 3. 后序遍历
    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

# 测试
if __name__ == '__main__':
    r = BinaryTree('a')
    # print(r.getRootVal())
    # print(r.getLeftChild())
    r.insertLeft('b')
    # print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    # print(r.getRightChild().getRootVal())
    r.insertLeft('d')
    # print(r.getLeftChild().getRootVal())    # d
    # print(r.getLeftChild().getLeftChild().getRootVal())   # b
    # r.preorder()    # 先序遍历
    # r.inorder()    # 中序遍历
    r.postorder()    # 后续遍历