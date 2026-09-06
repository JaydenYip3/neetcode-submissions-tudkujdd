class Solution:
    def rob(self, nums: List[int]) -> int:

        def houses(i: int, mem: dict) -> int:
            if i >= len(nums):
                return 0
            if i in mem:
                return mem[i]
            
            val = nums[i] 
            for house in range(i + 2, len(nums)):
                val = max(nums[i] + houses(house, mem), val)
            mem[i] = val  
            return mem[i] 
                
        return max(houses(0,{}), houses(1, {}))
        