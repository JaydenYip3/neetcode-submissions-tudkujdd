import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = 0

        while l <= r: 
            mid = (l + r) // 2
            temp_h = h
            for num in piles:
                temp_h -= math.ceil(num / mid)
                if temp_h < 0:
                    break 
            if temp_h >= 0:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return result    
        