class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternToWord, wordToPattern = {}, {}
        words = s.split(' ')
        if len(words) != len (pattern):
            return False
        
        for p,w in zip(list(pattern),words):
            if  p not in patternToWord and w not in wordToPattern:
                patternToWord[p] = w
                wordToPattern[w] = p
            elif p in patternToWord and w in wordToPattern:
                if patternToWord[p] != w  or wordToPattern[w] != p:
                    return False
            else:
                return False
        return True

        

    def wordPatternNotUnderstoodQuestinself(self, pattern: str, s: str) -> bool:
        patternCount = Counter(pattern)
        for c in s:
            if c in patternCount:
                patternCount[c] -=1
                if patternCount[c] == 0:
                    patternCount.pop(c)
        return patternCount == None