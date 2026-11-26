class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [amount + 1] * (amount + 1)
        table[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    table[a] = min(table[a], table[a - c] + 1)
        
        return table[-1] if table[-1] != (amount + 1) else -1 



        