class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        original = 26 * [0]
        for char in s1:
            original[ord(char) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
        check = 26 * [0]

        for i in range(r + 1):
            check[ord(s2[i]) - ord('a')] += 1

        if check == original:
            return True

        for r in range(len(s1), len(s2)):
            check[ord(s2[r]) - ord('a')] += 1
            check[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if check == original:
                return True

        return False