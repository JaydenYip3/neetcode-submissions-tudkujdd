class Solution:
    def climbStairs(self, n: int) -> int:    
        if n <= 2:
            return n
        step1, step2 = 1, 2 

        for step in range(3, n + 1):
            next_step = step1 + step2
            step1 = step2
            step2 = next_step

        return step2
        