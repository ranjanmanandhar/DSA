class MyHashMap:

    def __init__(self):
        self.size = 10001
        self.lists = [[] for _ in range(self.size)]
        
    def put(self, key: int, value: int) -> None:
        pairs = self.lists[key % self.size]
        print(pairs)
        for i, (k, v) in enumerate(pairs):
            if k == key:
                pairs[i] = (key, value)
                return
        pairs.append((key, value))

    def get(self, key):
        pairs = self.lists[key % self.size]
        for k, v in pairs:
            if k == key:
                return v
        return -1

    def remove(self, key):
        pairs = self.lists[key % self.size]
        for i, (k, v) in enumerate(pairs):
            if k == key:
                del pairs[i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(4,223)
param_2 = obj.get(4)
print(param_2)
# obj.remove(key)