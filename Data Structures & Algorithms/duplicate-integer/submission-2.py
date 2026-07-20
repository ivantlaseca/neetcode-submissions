"""
[1,1]
T

[1,2,3]
F

[]
F

[-1,1,2]
F

"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for n in range(len(nums)):
            if nums[n] in elements:
                return True
            elements.add(nums[n])
        return False