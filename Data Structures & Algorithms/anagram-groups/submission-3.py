class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        group = {}

        for word in strs:
            letters = tuple(sorted(word))
            if letters in group:
                group[letters].append(word)
            else:
                group[letters] = [word]
        
        for arr in group.values():
            result.append(arr)
        
        return result      

        