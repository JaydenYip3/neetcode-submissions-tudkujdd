class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, total, path):
            if total == target:
                result.append(path.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            backtrack(i, total + nums[i], path) 
            path.pop() 
            backtrack(i + 1, total, path) 
            
        backtrack(0, 0, [])
        return result
        