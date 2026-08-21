import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap. O(max(klogn, n)) time & O(n) space
        heap = [-num for num in nums]
        heapq.heapify(heap) # O(n) time
        for _ in range(k-1):
            heapq.heappop(heap)
        return - heapq.heappop(heap)