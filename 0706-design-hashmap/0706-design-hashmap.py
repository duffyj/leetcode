class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.hashMap.append((key,value)) 

    def get(self, key: int) -> int:
        for (k,v) in self.hashMap:
            if k == key:
                return v
        return -1        
        

    def remove(self, key: int) -> None:
        self.hashMap = [(k,v) for k,v in self.hashMap if k != key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

