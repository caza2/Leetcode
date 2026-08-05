class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # top-down memoization
        cache: dict[int, int] = {}
        def f(cost: list[int]) -> int:
            if len(cost) <= 1:
                return 0
            elif len(cost) == 2:
                return min(cost[0], cost[1])
            if len(cost) in cache:
                return cache[len(cost)]
            else:
                cache[len(cost)] = min(cost[-1] + f(cost[:-1]), cost[-2] + f(cost[:-2]))
                return cache[len(cost)]
        return f(cost)