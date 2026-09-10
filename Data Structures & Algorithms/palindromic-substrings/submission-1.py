class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r <= len(s) and s[l] == s[r - 1]:
                l -= 1
                r += 1
                result += 1
            l, r = i - 1, i + 1
            while l >= 0 and r <= len(s) and s[l] == s[r - 1]:
                l -= 1
                r += 1
                result += 1

        return result