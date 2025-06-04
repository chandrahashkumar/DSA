class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key)% self.size

    def insert(self,key,value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key,value)]
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index][i] == (key, value)
                    return
                self.table[index].append((key, value))

    def search(self,key):
        index = self._hash(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i]
                    return

# Usage example

hash_table = HashTable(10)
hash_table.insert("apple",5)
hash_table.insert("banana",3)
hash_table.insert("cherry",8)

print(hash_table.search("apple")) # 5
print(hash_table.search("banana")) # 3
print(hash_table.search("cherry")) # 8

hash_table.delete("banana")
print(hash_table.search("banana")) # None