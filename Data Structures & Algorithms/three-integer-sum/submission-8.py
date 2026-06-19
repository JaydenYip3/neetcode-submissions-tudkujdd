class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num1 = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                if num1 + nums[l] + nums[r] == 0:
                    result.append([num1, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  
                        r -= 1
                    l += 1
                    r -= 1
                elif num1 + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return result

                    






        