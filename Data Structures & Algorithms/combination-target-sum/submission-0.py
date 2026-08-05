class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output: List[List[int]] = []
        res: Optional[list[int]] = []
        nums.sort()
        hashSet: set[int] = set(nums)
        def backtrack(nums: List[int], target: int) -> None:
            for i in range(len(nums)):
                if not nums:
                    return
                if nums[i] > target : # Plus de combinaison possible
                    return        
                if target in hashSet and res + [target] not in output:
                    res.append(target)
                    output.append(res.copy())
                    res.pop()
                res.append(nums[i])
                backtrack(nums[i:], target-nums[i])
                res.pop()
            return
        backtrack(nums, target)
        return output