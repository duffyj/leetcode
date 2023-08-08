from collections import deque

"""
1. maintain a list of fresh oranges
2. count numer of fresh oranges
3. loop though fresh oranges:
    3.1 check of any are now rotten
    3.2 mark newly rotton in main array
    3.2 remove newly rotton from list of fresh oranges
4. Count remaining fresh oranges
    if no change in number of fresh then stop.
"""

class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        remaningFresh = set()
        ROWS, COLS = len(grid), len(grid[0])
        FRESH,EMPTY,ROTTEN = 0,1,2
        adjacents = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1. maintain a list of fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r,c] == FRESH:
                    remaningFresh.add((r,c))
        
        minutes = 0
        while True:
            minutes += 1
            newRotten = []
            for r,c in remaningFresh:
                for adjR,adjC in adjacents:
                    newR, newC = r+adjR, c+adjC
                    # check of any fresh are now rotten
                    if (newR > 0 and
                        newC > 0 and
                        newR < ROWS and
                        newC < COLS and
                        grid[newR][newC] == ROTTEN
                       ):
                        grid[r][c] = ROTTEN     # 3.2 mark newly rotton in main array
                        newRotten.append((r,c))
                        break
                    if not newRotten:
                        return -1  # if no change in number of fresh then stop.
                    for toRemove in newRotten:
                        remaningFresh.remove(toRemove)
        return minutes
                
                                        
                
                        
                
            
            
        
        



































































class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # This is a rotten orange
                # Then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
    
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        # setup rotten queue and count fresh
        freshOranges = 0
        iLen, jLen  = len(grid), len(grid[0])
        for i in range(iLen):
            for j in range(jLen):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    freshOranges += 1
                
        # add exit condition to queue
        queue.append((-1,-1))
        elaspedTime = -1
        adjustments = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            i,j = queue.popleft()
            if i == -1:
                elaspedTime +=1
                if queue:
                    queue.append((-1,-1))
            else:
                for iAdj, jAdj in adjustments:
                    iNext, jNext = i + iAdj, j + jAdj
                    if iLen > iNext >= 0 and jLen > jNext >= 0:
                        if grid[iNext][jNext] == 1:
                            grid[iNext][jNext]  = 2 # fresh will go rotten
                            freshOranges -=1
                            queue.append((iNext,jNext)) 
        
        return elaspedTime if freshOranges == 0 else -1   