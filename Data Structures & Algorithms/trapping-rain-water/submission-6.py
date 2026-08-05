class Solution:
    def trap(self, height: List[int]) -> int:
        reliefStack: list[int] = []
        i: int = 0 # itération sur height
        concavity: list[tuple[int, int]] = []
        while i < len(height) - 1:
            if not reliefStack and height[i] > height[i+1]:
                reliefStack.append(i)
                i += 1
            elif reliefStack and height[i] <= height[i+1]:
                i += 1
            elif reliefStack and height[i] > height[i+1]:
                if height[i] <= height[i-1]:
                    i += 1
                elif len(reliefStack) == 1:
                    reliefStack.append(i)
                    if height[i] >= height[reliefStack[0]]:
                        concavity.append(reliefStack)
                        reliefStack = []
                    else:
                        i += 1
                elif len(reliefStack) == 2:
                    if height[i] >= height[reliefStack[0]]:
                        reliefStack.pop()
                        reliefStack.append(i)
                        concavity.append(reliefStack)
                        reliefStack = []
                    elif height[i] >= height[reliefStack[1]]:
                        reliefStack.pop()
                        reliefStack.append(i)
                        i += 1
                    elif height[i] < height[reliefStack[1]]:
                        i += 1
            else:
                i += 1
        # on a concavity, donc toutes les vallées (locales, à voir après pour globale)
        if len(reliefStack) == 2:
            if height[-1] >= height[reliefStack[1]]:
                reliefStack.pop()
                reliefStack.append(len(height)-1)
            concavity.append(reliefStack)
        elif len(reliefStack) == 1:
            reliefStack.append(len(height)-1)
            concavity.append(reliefStack)
        area: int = 0
        for c in concavity:
            for k in range(c[0]+1, c[1]):
                area += max(0, min(height[c[0]], height[c[1]]) - height[k])
        return area
                