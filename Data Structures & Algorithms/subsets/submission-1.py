class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        subset: list[int] = []
        def backtrack(i: int) -> None:
            nonlocal subset
            # On a atteint le bout, il n'y a plus rien à ajouter dans subset
            if i == len(nums):
                res.append(subset.copy())
                return

            # Choix où on inclut nums[i] dans subset
            subset.append(nums[i])
            backtrack(i+1)
            
            # Choix où on exclus nums[i] de subset
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        return res