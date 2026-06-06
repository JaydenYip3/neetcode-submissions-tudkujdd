class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def stairs(cur: int, mem={}):
            if cur == n:
                return 1
            elif cur > n:
                return 0
            if cur in mem:
                return mem[cur] 
            mem[cur] = stairs(cur + 1) + stairs(cur + 2)
            return mem[cur] 
        
        return stairs(0)


        