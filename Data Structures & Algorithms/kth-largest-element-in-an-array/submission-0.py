class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        result = 0 

        while k > 0:
            result = heapq.heappop(nums)
            k -= 1
        
        return -result
            
        