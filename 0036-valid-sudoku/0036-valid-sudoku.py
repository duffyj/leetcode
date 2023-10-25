from collections import defaultdict, Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        blocks = defaultdict(list)

        for rowNum,row in enumerate(board,0):
            for colNum,val in enumerate(row,0):
                if val != ".":
                    xBlock = (colNum) // 3
                    yBlock = (rowNum) // 3
                    val  = int(val)
                    #if val > 9 or val < 1:
                    #if not 0 < val < 10:
                    #    return False
                    blockKey = (xBlock,yBlock)
                    if val in blocks[blockKey]:
                        return False
                    blocks[blockKey].append(val)

                    rowKey = (xBlock, rowNum)
                    if val in rows[rowKey]:
                        return False
                    rows[rowKey].append(val)

                    colKey = (yBlock, colNum)
                    if val in cols[colKey]:
                        return False
                    cols[colKey].append(val)
        
        # validate
        #sums = [sum(b) for b in blocks]
        #if any((s for s in (sum(b) for b in blocks) if s > 45)):
        #    return False

        for i in range(9):
            for rowCol in rows,cols:
                x = rowCol[0,i] + rowCol[1,i] + rowCol[2,i]
                #if sum(x) > 45:
                #    return False
                if any((k for k, v in Counter(x).items() if v > 1)):
                    return False
        return True

class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                if ch != '.':
                    triple = {(ch, r), (c, ch), (ch, c // 3, r // 3)}   # row, col, sub
                    if seen & triple: return False
                    seen |= triple
        return True   



