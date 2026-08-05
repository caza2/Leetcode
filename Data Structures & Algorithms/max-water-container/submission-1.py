class Solution:
    @staticmethod
    def computeArea(heights: list[int], i: int, j: int) -> int:
        return abs(i-j)*min(heights[i], heights[j])
    
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea: int = 0
        while left < right:
            area: int = Solution.computeArea(heights, left, right)
            if area > maxArea:
                maxArea = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea