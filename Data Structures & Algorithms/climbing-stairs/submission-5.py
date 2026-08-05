class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-up tabulation no memory O(1)
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n+1):
            prev, curr = curr, prev+curr
        return curr