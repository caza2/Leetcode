class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                hashmap[target - num].append(index)
            else:
                hashmap[target - num] = [index]
        for index, num in enumerate(nums):
            if num in hashmap and (index != hashmap[num][-1]):
                return [index, hashmap[num][-1]]