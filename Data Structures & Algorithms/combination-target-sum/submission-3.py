class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i: int, path: List[int]):
            if sum(path) == target:
                result.append(path.copy())
                return
              
            if i >= len(nums) or sum(path) > target:
                return 
            
            path.append(nums[i])
            backtrack(i, path)
            path.pop()
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return result


            

        