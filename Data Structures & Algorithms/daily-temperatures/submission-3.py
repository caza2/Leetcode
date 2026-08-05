class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output: list[int] = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                colder: tuple[int, int] = stack.pop()
                output[colder[0]] = index - colder[0]
            stack.append((index, temp))
        return output