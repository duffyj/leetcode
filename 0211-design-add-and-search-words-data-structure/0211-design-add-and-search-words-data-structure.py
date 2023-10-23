class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[None] = None

    def search(self, word: str, curr=None) -> bool:
        curr = curr or self.root
        for i,c in enumerate(word):
            if c == '.':
                return any((self.search(word[i+1:],subtree) for k,subtree in curr.items() if k != None))
            if c not in curr:
                return False
            curr = curr[c] 
        return None in curr.keys()
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)