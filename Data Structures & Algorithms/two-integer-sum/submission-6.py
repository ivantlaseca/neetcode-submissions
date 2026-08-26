class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {}
        for n in range(len(nums)):
            if target - nums[n] in numToIdx:
                return [numToIdx[target - nums[n]], n]
            numToIdx[nums[n]] = n
        
        