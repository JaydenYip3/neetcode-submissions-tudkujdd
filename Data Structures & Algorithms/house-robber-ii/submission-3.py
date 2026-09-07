class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        def dp(i: int, mem: dict(), nums: List[int]) -> int:
            rob1, rob2 = 0, 0

            for num in nums:
                temp = max(num + rob1,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
          
        return max(dp(0, {}, nums[:-1]), dp(1, {}, nums[1:]))