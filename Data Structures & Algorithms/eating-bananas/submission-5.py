class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatingTime(k: int) -> int:
            hours: int = 0
            for pile in piles:
                hours += (pile + k - 1)//k
            return hours
        k_lower, k_upper = 1, max(piles) # bounds
        min_k = max(piles)
        while k_lower < k_upper:
            middle: int = (k_upper + k_lower)//2
            if eatingTime(middle) <= h:
                min_k = min(min_k, middle)
                k_upper = middle
            else:
                k_lower = middle + 1
        return min_k
