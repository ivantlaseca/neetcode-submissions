class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elements = set(nums)
        return len(elements) != len(nums)
        