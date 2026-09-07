class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        edges.sort(key=lambda e: e[0])

        seen = set()
        for fr, to in edges:
            if fr in seen and to in seen:
                return False
            seen.add(fr)
            seen.add(to)
        
        return True
                         
        