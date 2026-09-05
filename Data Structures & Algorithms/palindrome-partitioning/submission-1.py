class Solution:
    def isPalindrome(self, s:str) -> bool:
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]: 
        res = []

        def backtrack(i: int, path: list[str]):
            if i == len(s):
                res.append(path.copy())
            for y in range(i, len(s)):
                if self.isPalindrome(s[i:y+1]):
                    path.append(s[i:y+1])
                    backtrack(y + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res


        



        