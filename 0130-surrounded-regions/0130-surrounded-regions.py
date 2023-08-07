class Solution:
    def solve(self, board: List[List[str]]) -> None:
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
            
        