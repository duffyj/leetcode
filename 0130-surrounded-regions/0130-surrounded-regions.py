"""

task - fip all Os that can be captured to an X.
     - all O not 4 way adjacent to an border 0 can be captured.
     - if 0 is connected to border O then it is safe and cannot be flipped to an X.
        
    Dfs staring at all border squares.
    mark all safe Os with another char (R?) 
    2nd phase of clean up which will be (n-2) *(m-2)
"""


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

class Solution:
    def solve2(self, board: List[List[str]]) -> None:
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def solve(self, board: List[List[str]]) -> None:        
        """
        Do not return anything, modify board in-place instead.
        """
        nRows = len(board) - 1        
        if nRows == 0:
            return
        nCols = len(board[0]) -1
        if nCols == 0:
            return
        
        # setup starting point
        toSearch = deque([(0,0)])
        visited = set()
        
        # add borders
        for r in range(0,nRows+1):
            for c in range(0,nCols+1):
                if (r  in  (0,nRows) or c in (0,nCols)):
                    toSearch.append((r,c))
                                                                                                    
        adjacents = [(1,0), (-1,0) , (0,1), (0,-1)]
        
        while(toSearch):
            r,c = toSearch.popleft()
            if (r,c) not in visited:
                visited.add((r,c))
                if board[r][c]  == 'O':
                    board[r][c] = 'R' # mark to retain
                    for rInc,cInc in adjacents:
                        rNew, cNew = r + rInc, c + cInc
                        if (0 <= rNew <= nRows) and (0 <= cNew <= nCols) and (rNew,cNew) not in visited and board[rNew][cNew]  == 'O':
                            toSearch.append((rNew,cNew))
         
        # add borders
        for r in range(0,nRows+1):
            for c in range(0,nCols+1):
                if board[r][c]  == 'O':
                    board[r][c] = 'X'
                if board[r][c]  == 'R':
                    board[r][c]  = 'O'
            
        