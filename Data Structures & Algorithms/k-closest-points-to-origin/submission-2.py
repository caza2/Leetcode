import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: list[tuple[float, int, int]] = []

        for x, y in points:
            heapq.heappush(heap, (-(x**2 + y**2), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]

