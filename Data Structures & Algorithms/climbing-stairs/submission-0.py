class Solution:
    def climbStairs(self, n: int) -> int:
        result = {} 

        def recursion(n: int) -> int:
            nonlocal result
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in result:
                return result[n] 
            
            result[n] = recursion(n - 1) + recursion(n - 2)
            return result[n]
        
        return recursion(n)

        