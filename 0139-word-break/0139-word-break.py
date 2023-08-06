class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[len(s)] = True

        for i in range(len(s),-1,-1):
            for w in  wordDict:
                if (i + len(w)) <= len(s):
                    if w == s[i:i+len(w)]:
                        dp[i] = dp[i+len(w)]
                    if dp[i]:
                        break
        return dp[0]




class SolutionGoOneCeap:
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        res = []
        currWord = ''
        possibleWords = wordDict[:]
        for letter in s:
            searchWord =  currWord + letter
            if possibleWords := [p for p in possibleWords if p.startsWith(searchWord)]:
                if [p for p in possibleWords if p == searchWord]:
                    # match
                    currWord = ''
                    continue
            if currWord:
                currWord = letter
                
            

        return True
