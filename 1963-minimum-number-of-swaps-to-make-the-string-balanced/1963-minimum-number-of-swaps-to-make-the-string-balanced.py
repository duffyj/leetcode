class Solution4:
    def minSwaps(self, s: str) -> int:
        req = 0
        res = 0
        for c in s:
            if c == '[':
                req -= 1             
            else:
                req +=1 
            if req == 0:
                res += 1
        return res

class Solution:
    def minSwaps(self, s: str) -> int:
        req = 0
        stack = []
        for c in s:
            if c == '[':
                stack.append('[')
            elif stack:
                stack.pop()
            else:
                req += 1
        return int((req +1) /2)    