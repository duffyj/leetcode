class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        seen = set()
        for i in range(9,len(s)):
            seq = s[i-9:i+1]
            if seq in seen:
                res.add(seq)
            seen.add(seq)
        return res
        