class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        max_r = len(grid)
        max_c = len(grid[0])
        directions = [[1,0],[0,1],[-1,0], [0,-1]]

        def dfs(r,c):
            if 0 > r or r >= max_r or 0 > c or c >= max_c or grid[r][c] ==  0 :
                return 0
            grid[r][c] =  0  

            total = 1 
            for dr,dc in directions:
                total += dfs(r + dr, c + dc)
            return total
        
        for r in range(max_r):
            for c in range(max_c):
                if grid[r][c] ==  1 : 
                    area = dfs(r,c)
                    max_area = max(area, max_area)

        
        return max_area


        