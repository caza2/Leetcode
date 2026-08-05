class Solution:
    def rob(self, nums: List[int]) -> int:
        cache: dict[int, int] = {}
        def f(n: int) -> int:
            if n in cache:
                pass
            elif n <= 0:
                cache[n] = 0
            elif n == 1:
                cache[n] = nums[0]
            else:
                cache[n] = max(f(n-1), nums[n-1] + f(n-2))
            return cache[n]
        return f(len(nums))