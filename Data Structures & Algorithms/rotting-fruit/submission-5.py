from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotting = []
        DIRECTIONS = [[1,0], [-1,0], [0,1], [0,-1]]
        num_fruits = 0
        num_rot = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotting.append((i,j))
                elif grid[i][j] == 1:
                    num_fruits += 1 
        
        time = 0
        while rotting:
            temp = []
            for rot in rotting:
                r,c = rot
                for d in DIRECTIONS:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            num_rot += 1
                            grid[nr][nc] = 2
                            temp.append((nc,nr))
            if not temp:
                pass
            else:
                time += 1
            rotting = temp
         
        return time if num_rot == num_fruits else -1 
            

                
        