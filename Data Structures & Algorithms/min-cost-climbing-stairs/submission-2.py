class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = len(cost)

        def climb(i: int, mem: dict) -> int:
            if i >= total:
                return 0 
            
            if i in mem:
                return mem[i]
                
            mem[i] = cost[i] + min(climb(i + 1, mem),climb(i + 2, mem)) 
            return mem[i]
        

        return min(climb(0, {}), climb(1,{}))
  