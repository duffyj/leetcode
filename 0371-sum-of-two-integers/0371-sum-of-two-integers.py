class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carryBit = 0
        for i in range(32):
            aBit = (a >> i ) & 1
            bBit = (b >> i ) & 1
          
            newCarry = 0
            newBit = 0        
            if carryBit:
                if aBit and bBit:
                    newCarry = 1
                    newBit = 1
                elif aBit or bBit:
                    newCarry = 1
                    newBit = 0
                else:
                    newBit = 1
            else:
                if aBit and bBit:
                    newCarry = 1
                    newBit = 0
                elif aBit or bBit:
                    newCarry = 0
                    newBit = 1
            if newBit:
                res = res | (newBit << i)
            carryBit = newCarry
            
        mask = 0xffffffff
        return (res | ~ mask)  if (res>>31) & 1 else res
                
                        
            
            
        