class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        turns = 0
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -= 1
            turns += 1           
        return turns if fresh == 0 else -1          
        