class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballonchars = list('balon') 
        charCounts = {c:0 for c in ballonchars}
        for t in text:
            if t in ballonchars:
                charCounts[t] += 1
        res = sys.maxsize
        for char,count in charCounts.items():
            if char in ('l','o'):
                count = count // 2
            res = min(res,count)
        return 0 if res == sys.maxsize else res 
