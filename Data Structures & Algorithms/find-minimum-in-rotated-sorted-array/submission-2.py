class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        elif len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left < right:
            middle: int = (left + right)//2
            if middle - 1 >= 0 and nums[middle-1] > nums[middle] :
                break
            if middle + 1 < len(nums) and nums[middle] > nums[middle+1]:
                return nums[middle+1]
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle
        return nums[middle]