class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sort = []
        for p , s in zip(position, speed):
            sort.append((p,s))
        sort.sort(reverse=True)

        result = []

        for item in sort:
            result.append((target - (item[0])) / item[1])
            if len(result) >= 2 and result[-1] <= result[-2]:
                result.pop()
        return len(result)