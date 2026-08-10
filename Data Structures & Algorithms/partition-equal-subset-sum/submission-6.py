class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Computation of initial list's sum
        S: int = 0
        for num in nums:
            S += num
        if S % 2:
            return False
        inpt: list[int] = nums + [0]

        # Cache initialization (hashmap)
        cache: dict[str, int] = {str(inpt): S}

        # Recursion function
        def f(l: list[int], index: int) -> Optional[bool]:
            if len(l) == 0:
                return
            copy: list[int] = l.copy()
            copy.pop(index)
            if str(copy) not in cache:
                cache[str(copy)] = cache[str(l)] - l[index]
            if cache[str(copy)] == S/2:
                return True
            elif cache[str(copy)] < S/2:
                return
            else:
                for i in range(len(copy)):
                    if f(copy, i):
                        return True
        
        if f(inpt, len(inpt)-1):
            return True
        return False
