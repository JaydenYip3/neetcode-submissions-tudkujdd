class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)

        prod = 1
        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums) -1, -1, -1):
            postfix[i] = prod
            prod *= nums[i]
 
        res =[0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        return res
        