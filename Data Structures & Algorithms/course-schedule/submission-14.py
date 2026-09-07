from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
 
        lookup = defaultdict(list)
        for course, prereq in prerequisites:
            lookup[course].append(prereq)

        visited = set()
        def dfs(prereq) -> bool:
            if prereq in visited:
                return False 
            if lookup[prereq] == []:
                return True
            visited.add(prereq)
            
            for p2 in lookup[prereq]:
                if not dfs(p2):
                    return False
            visited.remove(prereq)
            lookup[prereq] = []
            return True  
             
        for course, prereq in prerequisites:
            if not dfs(prereq):
                return False
        
        return True





        
                



        