class Node(object):
    
    def __init__(self):
        self.end = False
        self.next = [None] * 26


def cnum(c):
    return ord(c.lower()) - ord('a')

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            n = cnum(c)
            if curr.next[n] == None:
                curr.next[n] = Node()
            curr = curr.next[n]
        curr.end = True
            
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            n = cnum(c)
            if curr.next[n] == None:
                return False
            curr = curr.next[n]
        return curr.end == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            n = cnum(c)
            if curr.next[n] == None:
                return False
            curr = curr.next[n]
        return True

class TrieDict:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[None] = None
            
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c] 
        return None in curr.keys()

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c] 
        return True

    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)