class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Solution en O(n^2) time, O(n) space
        dp: list[int] = [1] # taille ddu LIS de nums[: key+1]
        for i in range(1, len(nums)):
            j: int = i-1
            localmaxLIS: int = 0
            while j >= 0:
                if nums[j] < nums[i]:
                    localmaxLIS = max(localmaxLIS, dp[j])
                j -= 1
            dp.append(1 + localmaxLIS)
        return max(dp)