class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up tabulation
        table = [0] * (n+1)
        table[1] = 1
        if n <= 1:
            return table[n]
        table[2] = 2

        for i in range(3, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[-1]