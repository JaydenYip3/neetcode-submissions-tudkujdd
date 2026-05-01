class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = [] 
        freq = defaultdict(int) 

        for task in tasks:
            freq[task] += 1

        for k,v in freq.items():
            q.append([-v,k])  
        
        heapq.heapify(q)
        q2 = collections.deque() 
        turns = 0

        while q or q2:
            turns += 1
            if q2 and q2[-1][0] == turns:
                _, task = q2.pop()
                heapq.heappush(q, task)
            if q:
                task = heapq.heappop(q)
                ready = n + turns + 1
                task[0] += 1
                if task[0] < 0:
                    q2.appendleft([ready,task])
        return turns 


        