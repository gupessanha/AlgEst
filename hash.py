class hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))
            
    def printTable(self):
        for i in range(self.size):
            print(i, end = " ")
            for j in self.table[i]:
                print("-->", end = " ")
                print(j, end = " ")
            print()
            
        
        
hash = hash_table(10)
hash.insert(10, "Nepal")
hash.insert(25, "EUA")
hash.insert(20, "India")
hash.insert(9, "Australia")
hash.insert(21, "Japão")

hash.printTable()