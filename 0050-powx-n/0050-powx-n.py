class Solution:

    def myPow(self, x: float, n: int) -> float:
        def helper(v,n):
            if n == 1:
                return v
            if n == 0:
                return 1
            if v == 0:
                return 0
            if n%2:
               nMinus1 = n-1 
               yy = helper(v,nMinus1/2)
               return v * yy * yy 
            else:
                xx = helper(v,n/2)
                return  xx * xx
                
        res = helper(x,abs(n))
        return res if n > 0 else  1/res
            
    def myPowSloe(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        v = 1.0
        for _ in range(abs(n)):
            v *=x
        return v if n > 0 else  1/v

        