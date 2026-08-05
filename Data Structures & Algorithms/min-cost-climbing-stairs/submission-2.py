class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # top-down memoization
        cache: dict[int, int] = {}
        def f(n: int) -> int:
            if n <= 1:
                return 0
            if n in cache:
                return cache[n]
            else:
                cache[n] = min(cost[n-1] + f(n-1), cost[n-2] + f(n-2))
                return cache[n]
        return f(len(cost))