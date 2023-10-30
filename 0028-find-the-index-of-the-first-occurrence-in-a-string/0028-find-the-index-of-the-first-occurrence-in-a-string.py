class SolutionMine:
    def strStr(self, haystack: str, needle: str) -> int:
        n = 0
        h = 0
        while h < len(haystack) :
            if haystack[h] == needle[n]:
                n +=1
                if n == len(needle):
                    return h - len(needle) +1
            else:
                h -= n
                n = 0
            h += 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for h in range(len(haystack) - len(needle) +1):
            if haystack[h:h+len(needle)] == needle:
                return h
        return -1