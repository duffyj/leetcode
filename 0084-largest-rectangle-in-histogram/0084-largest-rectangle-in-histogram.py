import sys

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        heights.append(0)
        for x in range(len(heights)):
            rY,rX = 0,x
            while stack and stack[-1][0] > heights[x]:
                rY,rX = stack[-1]
                result = max(result, (x-rX) * rY)
                stack.pop()
            if not stack or stack[-1][0] < heights[x]:
                stack.append((heights[x],rX))
        return result
        

class SolutionSlow2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        heightCounts = {}
        
        for currX in range(len(heights)):
            heightsEnded = tuple((colHeight,heightLen) for (colHeight,heightLen) in heightCounts.items() if colHeight > heights[currX])
            for colHeight,heightLen in heightsEnded:
                result = max(result, colHeight * heightLen)
                del  heightCounts[colHeight]
            for h in range(1,heights[currX]+1):
                if h not in heightCounts:
                    heightCounts[h] = 1
                else:
                    heightCounts[h] +=1 
            if heights[currX] not in heightCounts:
                heightCounts[heights[currX]] = 1
        
        for colHeight,heightLen  in heightCounts.items():
                result = max(result, colHeight * heightLen)

        return result



import sys
class SolutionVersionSlow:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        rowMin = sys.maxsize 
        row = []
        for i,h in enumerate(heights):
            if h > 0:
                rowMin = min(rowMin,h)
                row.append((i,h))

        while row:
            rowTotal = 0
            nextMin = sys.maxsize 
            nextRow = []
            while row:
                x,y  = row.pop()
                if y >= rowMin:
                    if y > rowMin:
                        nextMin = min(nextMin,y)
                        nextRow.append((x,y))
                    
                    rowTotal += 1
                    result = max(result, rowTotal * rowMin)
                    if not row or  abs(x-row[-1][0]) !=1:
                        rowTotal = 0
            row = nextRow
            rowMin = nextMin
        return result
            
