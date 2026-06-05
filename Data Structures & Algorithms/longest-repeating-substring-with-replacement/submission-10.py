class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = [0] * 26
        l = 0
        max_f = 0

        for r in range(len(s)):
            letters[ord(s[r]) - ord('A')] += 1
            max_f = max(max_f, letters[ord(s[r]) - ord('A')])
            diff = r - l + 1 - max_f

            if diff > k:
                letters[ord(s[l]) - ord('A')] -= 1
                l += 1
        
        return r - l + 1 






        