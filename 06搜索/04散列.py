# 散列函数
# 1.可以使用ord函数获取对应的ASCII值
# print(ord('c'))


# 为字符串构建简单的散列函数
# def hash(astring, tablesize):
#     sum = 0
#     for pos in range(len(astring)):
#         sum = sum + ord(astring[pos])
#     return sum % tablesize
#
# if __name__ == '__main__':
#     ha = hash('abc', 11)
#     # print(ha)

# --------------------------HashTable类-------------------------------#
class HashTable:
    def __init__(self):
        self.size = 11    # 散列表的初始大小
        self.slots = [None] * self.size    # 用于存储键
        self.data = [None] * self.size    # 用于存储值

    # put函数假设,除非键已经在self.slots中，否则总是可以分配一个空槽
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] == key
            self.data[hashvalue] == data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # 替换
            else:    # 下面的代码解决冲突问题
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data    # 替换

    def hashfunction(self, key, size):
        return key % size

    # 冲突之后再次进行hash
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    # get函数也先计算初始散列值
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    # hashtable类的最后两个方法提供了额外的字典功能
    # 重载__getitem__和__setitem__方法，以通过[]进行访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# 测试
if __name__ == '__main__':
    H = HashTable()
    H[2] = 'cat'
    H[3] = "dog"
    H[4] = "lion"
    H[5] = "bird"
    H[6] = 'cow'
    H[44] = 'goat'
    H[55] = 'pig'
    H[20] = 'chicken'
    H[21] = 'chicken'
    H[22] = 'chicken'
    print(H.slots)
    print(H.data)
    print(H[20])













