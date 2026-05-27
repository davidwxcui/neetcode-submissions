class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction= [[1,0],[-1,0],[0,-1],[0,1]]
        col_len= len(grid)
        row_len= len(grid[0])
        max_area=0
        local_max=0
        def dfs(c,r):
            nonlocal local_max
            if r<0 or r >= row_len or c<0 or c>=col_len or grid[c][r]==0:
                return
            grid[c][r]=0
            local_max +=1
            for x,y in direction:
                dfs(c+x,r+y)


        for i in range(col_len):
            for j in range(row_len):
                if grid[i][j]==1:
                    dfs(i,j)
                    max_area= max(max_area, local_max)
                    local_max=0
        return max_area