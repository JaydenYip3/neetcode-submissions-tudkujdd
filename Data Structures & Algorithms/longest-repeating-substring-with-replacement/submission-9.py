class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = [0]*26
        max_f = 0
        l = 0

        for r in range(len(s)):
            characters[ord(s[r]) - ord('A')] += 1
            max_f = max(max_f, characters[ord(s[r]) - ord('A')])
            diff = r - l + 1 - max_f

            if diff > k:
                characters[ord(s[l]) - ord('A')] -= 1
                l += 1
                
        return r -l + 1
            
        