class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int) 

        for num in nums:
            freq[num] += 1
        
        res = list(freq.items())

        res.sort(reverse=True, key=lambda x: x[1])

        return [x[0] for x in res[0:k]]

        