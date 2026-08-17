import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            self.nums.append(-num)
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        _temp: list[int] = self.nums.copy()
        for _ in range(self.k-1):
            heapq.heappop(_temp)
        return -heapq.heappop(_temp)
       