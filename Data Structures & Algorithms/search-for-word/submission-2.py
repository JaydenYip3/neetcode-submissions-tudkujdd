class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set() 
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(x: int, y: int, i: int) -> bool:
            if i == len(word): 
                return True
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or word[i] != board[x][y] or (x,y) in path:
                return False  
            
            path.add((x,y))
            found = backtrack( x + 1, y, i+1) or backtrack( x - 1, y, i+1) or backtrack( x, y + 1, i+1) or backtrack( x, y - 1, i+1)
            path.remove((x,y))
            return found
        
        
        for x in range(ROWS):
            for y in range(COLS):
                if backtrack(x, y, 0):
                    return True  
        
        return False           

        