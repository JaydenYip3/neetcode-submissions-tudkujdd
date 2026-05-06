class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        find = {}
        resLen, res = float("infinity"), [-1,-1]

        for c in t:
            find[c] = find.get(c, 0) + 1
        
        find_total = len(find)

        have = {}   
        have_total = 0
        l = 0    

        for r in range(len(s)):
            if s[r] in find:
                have[s[r]] = have.get(s[r], 0)  + 1

                if have[s[r]] == find[s[r]]:
                    have_total += 1
                
            while have_total == find_total:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                if s[l] in find:
                    have[s[l]] -= 1
                    if have[s[l]] < find[s[l]]:
                        have_total -= 1
                l += 1

        return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""
                



        