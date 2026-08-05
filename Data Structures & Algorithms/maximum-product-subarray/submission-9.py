class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[-1]
        minProd = nums[-1]
        prev, curr = None, nums[-1] 
        for i in range(len(nums)-2, -1, -1):
            prev, curr = curr, max(nums[i], nums[i] * curr, nums[i] * minProd)
            minProd, res = min(nums[i], nums[i] * prev, nums[i] * minProd), max(res, curr)
        return res