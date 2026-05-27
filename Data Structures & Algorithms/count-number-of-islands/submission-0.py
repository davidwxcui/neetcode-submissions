class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[1,0], [-1, 0], [0,-1],[0,1]]
        row_len= len(grid[0])
        col_len=len(grid)
        count=0

        def dfs(c,r):
            if c<0 or r<0 or c>=col_len or r>= row_len or grid[c][r]=="0":
                return
            grid[c][r]= "0"
            for x, y in directions:
                dfs(c+x,r+y)
        

        for c in range(col_len):
            for r in range(row_len):
                if grid[c][r]== "1":
                    dfs(c,r)
                    count+=1
        return count



