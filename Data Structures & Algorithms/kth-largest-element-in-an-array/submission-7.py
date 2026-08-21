class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quickselect algorithm O(n) time average, O(n^2) worst case time,O(1) space
        k: int = len(nums) - k
        def quickselect(l: int, r: int) -> int:
            pivot, p = nums[r], l # pivot value and pivot pointer
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                return quickselect(p+1, r)
            elif p > k:
                return quickselect(l, p-1)
            else:
                return pivot
        return quickselect(0, len(nums)-1)