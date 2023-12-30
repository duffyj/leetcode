class MyHashSet:

    def __init__(self):
        self.hashSet = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key) 

    def remove(self, key: int) -> None:
        self.hashSet = [k for k in self.hashSet if k != key]

    def contains(self, key: int) -> bool:
        for k in self.hashSet:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)