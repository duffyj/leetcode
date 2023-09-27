class Solution:

    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            newN = sum([int(n)**2 for n in str(n)])
            if newN == 1:
                return True
            if newN in seen:
                return False
            seen.add(newN)
            n = newN


    def isHappy1(self, n: int) -> bool:

        numbers = {}
        while n not in numbers:
            if n == 1:
                return True
            numbers[n] = n
            n = sum(int(s) ** 2 for s in str(n))
        return False

