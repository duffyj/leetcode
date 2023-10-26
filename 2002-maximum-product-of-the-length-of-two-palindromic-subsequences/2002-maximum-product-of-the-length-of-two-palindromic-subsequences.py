class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        maxBit = pow(2,n)
        pal = {}
        for i in range(1,maxBit+1):
            bitmask = i
            currPal = []
            for charnum in range(len(s)):
                bitmask = i >> charnum
                #print(bin(bitmask))                
                if bitmask & 1:
                    currPal.append(s[charnum])

            if currPal and currPal[0] == currPal[-1]:
                currPalStr = ''.join(currPal)
                if currPalStr == currPalStr[::-1]:
                    # add palindrom
                    currPalLen = len(currPalStr)
                    if currPalLen not in  pal:
                        pal[currPalLen] = []
                    pal[currPalLen].append(i)

        res = 0
        allPals = []
        for l in range(1,max(pal.keys())+1):
            if l in pal:
                allPals += [(l,i) for i in pal[l]]

        while allPals:
           level,larget = allPals.pop()
           for otherLevel, nextlargets in allPals:
                if not larget & nextlargets:
                    res = max(res,level * otherLevel)
            

        return res

        