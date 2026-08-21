import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        (i) Take the - minimum (max of the original heap) - w/ heappop
        (ii) Take the 2nd -minimum (2nd max of the original array)
        apply (i) - (ii) and append the result to the heap
        heappush the result (will also arrange in log n)
        Time O(n), Space O(n)
        """
        new_arr: list[int] = [-num for num in stones]
        minHeap: list[int] = new_arr.copy()
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            first_max, scnd_max = - heapq.heappop(minHeap), - heapq.heappop(minHeap)
            if first_max == scnd_max:
                continue
            else:
                heapq.heappush(minHeap, - first_max + scnd_max)
        return - heapq.heappop(minHeap) if minHeap else 0
