class Solution:
    def longestPalindrome(self, s: str):
        res = ""
        def doLongestPalindrome(j):
            finalL, finalR = j,j
            for startL,startR in (0,0), (0,1):
                r = j + startR
                l = j + startL
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r-l) > (finalR-finalL):
                        finalL,finalR = l,r
                    l -=1
                    r +=1
            return s[finalL:finalR+1]        
        for i in range(len(s)):
            pal = doLongestPalindrome(i)
            if len(pal) > len(res):
                res = pal
        return res


































































class Solutionbad:
    def longestPalindrome(self, s: str):
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r +=1
            return l,r

        maxl, maxr = 0, 0
        for i in range(len(s)):  
            for l,r in expand(i,i), expand(i,i+1):
                if (r-l) > (maxr-maxl):
                    maxl,maxr = l,r
        return s[maxl:maxr]

class Solution2:
    def longestPalindrome(self, s: str):
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r +=1
            return r -l- 1

        maxlen, start, end = 0,0,0
        for i in range(len(s)):  
            l = max(expand(i,i),expand(i,i+1))
            if l > end - start:
                start = i - (l-1)//2
                end = i + l//2
        return s[start:end+1]



class SolutionGood:
    def longestPalindrome(self, s: str) -> str:
        if s is '': 
            return s
        max_len = 0 
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]

    def expandFromCenter(self, s, idx1, idx2):
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
        return idx2 - idx1 - 1 
