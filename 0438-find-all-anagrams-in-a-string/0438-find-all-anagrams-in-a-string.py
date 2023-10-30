from collections import Counter
class SolutionSlow:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s) -1
        l = 0
        pCount = dict(Counter(p))
        zeroCount = {k:0 for k in pCount}
        res = []
        lenp = len(p)
        while l <= (n - lenp+1):
            if s[l] in p:
                currCount = dict(zeroCount)
                r = l
                while r < (l + lenp):
                    if s[r] not in currCount:
                        break
                    currCount[s[r]] +=1
                    r +=1
                if currCount == pCount:
                    res.append(l)
            l +=1     
        return res
                
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        res = []
        for i in range(ns):
            s_count[ord(s[i]) - ord('a')] += 1 # add next in window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')]  -= 1# remove old char
            
            if s_count == p_count:
                res.append(i - np + 1)
            
        
        return res
        
                
        