import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap. O(max(klogn, n)) time & O(n) space
        heap: list[int] = []
        for num in nums:
            heapq.heappush(heap, - num)
            if len(heap) > len(nums) - k + 1:
                heapq.heappop(heap)
        return - heapq.heappop(heap)