from random import choice
class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.keys = []        


    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.keys.append(val)
        self.data[val] = len(self.keys) -1
        return True

    def remove(self, val: int) -> bool:
        if val in self.data:
            # remove element and shrink list by one
            # e.g. mnove last item in keys to the one place of the one being removed
            indexToRemove = self.data[val]
            del self.data[val]
            lastItem = self.keys[-1]
            if lastItem != val:
                # unless the last item is the one being removed
                self.keys[indexToRemove] = lastItem
                self.data[lastItem] = indexToRemove
            self.keys.pop()
            return True
        return False        


    def getRandom(self) -> int:
        return choice(self.keys)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
D {0:0}
K [0]


indexToRemove = 0
D {}
K [0]




R 0
R O
I 0
GR
R 0 
I 0

"""