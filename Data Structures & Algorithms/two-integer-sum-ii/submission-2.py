class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            raise(ValueError("Pas de solution car numbers est vide."))
        left: int = 0
        right: int = len(numbers) - 1
        while numbers[right] + numbers[left] != target:
            if numbers[right] + numbers[left] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]