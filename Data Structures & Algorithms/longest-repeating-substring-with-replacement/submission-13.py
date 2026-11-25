class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        characters = [0] * 26

        res = 0
        l = 0
        for r in range(len(s)):
            characters[ord(s[r]) - ord('A')] += 1
            if r - l + 1 - max(characters) <= k:
                res = max(res, r - l + 1)
            else:
                while l < r and r - l + 1 - max(characters) > k:
                    characters[ord(s[l]) - ord('A')] -= 1
                    l += 1
        
        return res
               
        