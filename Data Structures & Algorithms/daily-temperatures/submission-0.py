class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output: list[int] = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(j-i)
                    break
            if len(output) < i + 1: # aucune journée plus chaude n'a été trouvée
                output.append(0)
        return output