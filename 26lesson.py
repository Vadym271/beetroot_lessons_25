def binary_presence(ilist, item):
    if item > ilist[-1] or item < ilist[0]:
        return False

    l = len(ilist)
    i = l // 2

    if ilist[i] == item:
        return True

    if item > ilist[i]:
        list2 = ilist[i + 1::]
        return binary_presence(list2, item)
        
    if item < ilist[i]:
        list2 = ilist[:i]
        return binary_presence(list2, item)

def binary_search(ilist, item, j = 0):
    """comment on meaning of variables:
    i represents the middle of current list
    j represents the beginning of count with respect to original list
    i_item represents current dividing element with respect to original list"""
    if item > ilist[-1] or item < ilist[0]:
        return None

    l = len(ilist)
    i = l // 2
    i_item = j + i

    if ilist[i] == item:
        return i_item

    if item > ilist[i]:
        list2 = ilist[i + 1::]
        return binary_search(list2, item, i_item + 1)

    if item < ilist[i]:
        list2 = ilist[:i]
        return binary_search(list2, item, i_item - i)


mylist = [i for i in range(12)]
print(binary_presence(mylist, 12))
print(binary_search(mylist, 22))

#task 2

class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(9)]
        self.size = 0

    def __setitem__(self, key, value):
        i = hash(key) % len(self.table)
        bucket = self.table[i]
        for j, (k, _) in enumerate(bucket):
            if k == key:
                bucket[j] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

    def __len__(self):
        return self.size

    def __contains__(self, key):
        i = hash(key) % len(self.table)
        return any(k == key for k, _ in self.table[i])

table = HashTable()
table[67] = "six-seven"
table[42] = "everything"
table[37] = "veritasium"

print(len(table))
