class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        #return sum([int(x) for x in bin(n)[2:]])