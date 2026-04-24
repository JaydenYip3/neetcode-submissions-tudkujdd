class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)  
            stone2 = -heapq.heappop(maxHeap) 

            if stone1 == stone2:
                continue
            stone3 = stone2 - stone1 if stone2 > stone1 else stone1 - stone2

            heapq.heappush(maxHeap, -stone3) 

        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
        
        