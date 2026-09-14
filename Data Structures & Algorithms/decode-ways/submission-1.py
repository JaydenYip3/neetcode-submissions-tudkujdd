class Solution:
    def numDecodings(self, s: str) -> int:
        mappings = {}
        for i in range(26):
            mappings[str(i + 1)] = chr(65 + i)

        mem = {}

        def recursion(i: int) -> int:
            if i >= len(s):
                return 1
            if i in mem:
                return mem[i]

            count = 0
            if s[i:i+1] in mappings:
                count += recursion(i + 1)
            if i <= len(s) - 2 and s[i:i+2] in mappings:
                count += recursion(i + 2)

            mem[i] = count
            return count

        return recursion(0)