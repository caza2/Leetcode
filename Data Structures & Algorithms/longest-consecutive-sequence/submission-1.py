class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset: set[int] = set(nums)
        decremented: set[int] = set([num-1 for num in nums]) & hashset
        k: int = 1
        while (len(decremented) != 0) and (decremented & hashset != {}):
            k += 1
            decremented = {num - 1 for num in decremented}
            decremented =  decremented & hashset
        return k
        
        
        