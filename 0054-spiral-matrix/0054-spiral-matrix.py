class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nR = len(matrix)
        nC = len(matrix[0])
        nRes = nR * nC
        res = []
        lBound, rBound, dBound, uBound = -1, nC, 0, nR 
        r,c = 0, 0
        while lBound < rBound and dBound < uBound:

            # move right
            while c < rBound:
                res.append(matrix[r][c])
                if len(res) == nRes:
                    return res
                c+= 1
            rBound -=1
            c -=1
            r +=1

            # move up
            while r < uBound:
                res.append(matrix[r][c])
                if len(res) == nRes:
                    return res
                r +=1
            uBound -=1
            r -=1
            c -=1

            # move left
            while c > lBound:
                res.append(matrix[r][c])            
                if len(res) == nRes:
                    return res
                c -=1
            lBound +=1
            c +=1 
            r -=1 

            # move down
            while r > dBound:
                res.append(matrix[r][c])
                if len(res) == nRes:
                    return res
                r -=1
            dBound +=1
            r +=1
            c +=1            




    def spiralOrderCrap(self, matrix: List[List[int]]) -> List[int]:
        adjustments = deque([(0,1), (1,0), (0,-1), (-1,0)])
        nR = len(matrix)
        nC = len(matrix[0])
        nRes = nR * nC
        results = [None] * nRes
        results[0] = matrix[0][0]
        self.lBound, self.rBound, self.dBound, self.uBound = -1, nC, -1, nR   
        def isInBound(r,c):
            if r <= self.dBound:
                self.dBound+=1
                return False
            if r >= self.uBound:
                self.uBound-=1
                return False
            if c <= self.lBound:
                self.lBound+=1
                return False
            if c >= self.rBound:
                self.rBound-=1
                return False                 
            return True

        resPos, r,c = 1, 0,0
        while True:
            adjR, adjC = adjustments.popleft()
            while True:
                if  isInBound(r+adjR,c+adjC):
                    r += adjR
                    c += adjC                    
                    print((r,c))
                    results[resPos] = matrix[r][c]
                    resPos +=1
                    if resPos == nRes:
                        return results
                else:
                     adjustments.append((adjR, adjC))
                     break
        