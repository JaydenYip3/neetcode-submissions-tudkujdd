class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int) 

        for num in nums:
            count[num] += 1
        
        
        return max(count.items(), key= lambda item: item[1])[0]
        