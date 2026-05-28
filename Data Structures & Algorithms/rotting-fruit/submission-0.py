class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS= len(grid)
        COLS= len(grid[0])
        q=deque()
        minutes=0
        fresh=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1

        while q and fresh>0:
            size=len(q)
            
            for _ in range(size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc= r+dr, c+dc

                    if (
                        0<=nr < ROWS and
                        0<= nc< COLS and
                        grid[nr][nc]==1 
                    ):
                        grid[nr][nc]= 2
                        fresh-=1
                        q.append((nr,nc))

            minutes+=1

        return minutes if fresh ==0 else -1