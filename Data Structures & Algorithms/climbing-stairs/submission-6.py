class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(step: int, cache: dict):
            if step > n:
                return 0
            if step == n:
                return 1  
            
            if step in cache:
                return cache[step]
            
            cache[step] = rec(step + 1, cache) + rec(step + 2, cache) 
            
            return cache[step]
        
        return rec(0, {})
        