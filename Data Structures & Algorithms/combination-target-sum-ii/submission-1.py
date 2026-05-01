class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(i, total, path):
            if total == target: 
                result.append(path.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            path.append(candidates[i])
            backtrack(i + 1, total + candidates[i], path) 
            path.pop()
            
            next_i = i + 1
            while next_i < len(candidates) and candidates[i] == candidates[next_i]:
                next_i += 1
            backtrack(next_i, total, path)
            
        backtrack(0, 0, [])
        return result
            
            

        