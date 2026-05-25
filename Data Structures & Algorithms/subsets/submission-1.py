class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 

        def backtrack(path: List[int], i):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()
            backtrack(path, i + 1)
            
        
        backtrack([], 0)
        return result
        