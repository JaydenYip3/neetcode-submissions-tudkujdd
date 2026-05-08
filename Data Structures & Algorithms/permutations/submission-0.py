class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path : List[int]):
            if len(path) == len(nums):
                result.append(path.copy()) 
                return 
            
            for index in range(len(nums)):
                if nums[index] in path:
                    continue
                path.append(nums[index])
                backtrack(path)
                path.pop()
        
        backtrack([])
        return result
            


        