class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            toMatch: int = target - numbers[i] # sera positif sinon nombre trouvé avant
            j: int = i+1
            while j < len(numbers) and numbers[j] <= toMatch:
                if numbers[j] == toMatch:
                    return [i+1, j+1]
                else:
                    j += 1
            continue