import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]

        heapq.heapify(stones)

        while len(stones) >= 2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            diff = abs(a - b)

            if diff == 0:
                continue
            else:
                heapq.heappush(stones, -diff)
        
        return -stones[0] if stones else 0   
        