"""
[3,4] t = 7

{
3 : 0
}

T: O(n)
S: O(n)

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimizations
        
        elementToIdx = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in elementToIdx:
                return [elementToIdx[diff], i]
            elementToIdx[nums[i]] = i

        