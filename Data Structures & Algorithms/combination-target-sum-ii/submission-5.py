class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output: list[list[int]] = []
        res: list[int] = []
        def backtrack(candidates: list[int], target: int) -> None:
            for i in range(len(candidates)):
                res.append(candidates[i])
                if i > 0 and candidates[i] == candidates[i-1]:
                    res.pop()
                    return
                if candidates[i] == target:
                    output.append(res.copy()) 
                    res.pop()
                    return
                if candidates[i] > target:
                    res.pop()
                    return
                if i < len(candidates) - 1:
                    backtrack(candidates[i+1:], target - candidates[i])
                res.pop()
            return
        backtrack(candidates, target)
        return output