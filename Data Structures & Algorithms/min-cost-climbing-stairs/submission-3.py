class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Bottom-up tabulation
        """
        if len(cost) <= 1:
            return 0
        prev, curr = 0, min(cost[0], cost[1])
        for i in range(2, len(cost)):
            prev, curr = curr, min(prev + cost[i-1], curr + cost[i])
        return curr
            