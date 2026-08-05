class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n: int = len(heights)
        left, right = [-1] * n, [n] * n # index du premier plus petit à gauche et du premier plus petit à droite
        stack: list = []
        for i in range(n): # remplissage de left
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack: list = [] # remplissage de right
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        max_area: int = 0 # calcul de l'aire
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area