
























from functools import cache



class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

    
        @cache
        def lcs(s1,s2):
            if s1 and s2:
                if s1[0] == s2[0]:
                    return 1 + lcs(s1[1:],s2[1:])
                else:
                    return max(lcs(s1[1:],s2),lcs(s1,s2[1:]))
            return 0

        return lcs(text1,text2)





class SolutionCrap:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = []
        for p1 in range(len(text1)):
            start = res[-1]+1 if res else 0
            for p2 in range(start,len(text2)):
                if text1[p1] == text2[p2]:
                    res.append(p2)
                    break
        
        return len(res)


class Solutionslow:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def lcs(s1,s2):

            if s1 and s2:
                if s1[0] == s2[0]:
                    return 1 + lcs(s1[1:], s2[1:])
                else:
                    return max(lcs(s1, s2[1:]),lcs(s1[1:], s2))
            return 0

        return lcs(text1,text2)


class Solutionslow:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def lcs(s1,s2):
            if s1 and s2:
                return (1 + lcs(s1[1:], s2[1:])) if s1[0] == s2[0] else max(lcs(s1, s2[1:]),lcs(s1[1:], s2))
            return 0

        return lcs(text1,text2)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1), len(text2)
        res = [[0] * (M+1) for _ in range(N+1)]
        
        for n in range(N):
            for m in range(M):
                if text1[n] == text2[m]:
                    res[n+1][m+1] = 1 + res[n][m]
                else:
                    a = res[n+1][m]
                    b = res[n][m+1]
                    res[n+1][m+1] = max(a,b) 

        return res[-1][-1]
