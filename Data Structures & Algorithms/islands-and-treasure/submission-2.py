class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        def bfs(r,c):  
            DIRECTIONS = [[1,0],[0,1], [-1,0],[0,-1]]
            visited = [[False] * COLS for _ in range(ROWS)]
            q = deque([(r,c)])
            visited[r][c] = True
            steps = 0
  
            while q:
                for _ in range(len(q)): 
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr,dc in DIRECTIONS:
                        nr = dr + row
                        nc = dc + col
                        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and grid[nr][nc] != -1:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                steps += 1   
            return INF
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)            