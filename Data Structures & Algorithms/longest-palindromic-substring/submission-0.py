class Solution:
    def longestPalindrome(self, s: str) -> str: 
        final = ""

        for index in range(len(s)):
            mid, l,r = index, index, index + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            res1 = s[l + 1:r]

            l,r = mid - 1, mid + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            res2 = s[l + 1:r]

            if len(final) > max(len(res1), len(res2)):
                continue
 
            elif len(res1) > max(len(final), len(res2)):
                final = res1
            else:
                final = res2

        return final
            


        