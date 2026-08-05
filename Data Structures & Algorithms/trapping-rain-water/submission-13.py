class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution avec stack. O(n) in time & space
        stack: list[int] = []
        water: int = 0
        
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom: int = stack.pop()
                if not stack:
                    break
                left: int = stack[-1]
                width: int = i - left - 1
                bounded_height: int = min(height[left], h) - height[bottom]
                water += width * bounded_height

            stack.append(i)
        
        return water