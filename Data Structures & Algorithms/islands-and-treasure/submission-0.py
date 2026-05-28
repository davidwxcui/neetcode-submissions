class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf= (2**31)-1
        direction=[[1,0],[-1,0],[0,1],[0,-1]]

        Rows= len(grid)
        Cols= len(grid[0])
        def dfs(r,c):
            q= deque([(r,c)])
            visit= [[False] * Cols for _ in range (Rows)]
            visit[r][c]= True
            steps=0
            while q:
                for _ in range(len(q)):
                    row, col= q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in direction:
                        nr, nc= row+dr, col+dc
                        if (0<= nr < Rows and 0<= nc <Cols and not visit[nr][nc] and grid[nr][nc]!=-1):
                            visit[nr][nc]=True
                            q.append((nr,nc))
                steps+=1
            return Inf

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j]==inf:
                    grid[i][j]=dfs(i,j)

    
        