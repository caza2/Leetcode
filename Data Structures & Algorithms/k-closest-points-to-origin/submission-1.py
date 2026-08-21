import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(point: list[int]) -> float:
            return point[0]**2 + point[1]**2

        arr: list[tuple[float, list[int]]] = []
        for point in points: # O(n) time
            arr.append((get_distance(point), point))
        heapq.heapify(arr) # Time O(n)
        output: list[list[int]] = []
        while len(output) != k:
            output.append(heapq.heappop(arr)[-1])
        return output
