class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        
        for num in nums:
            currentLength = 1
            currentNum = num
            while currentNum + 1 in numbers:
                currentLength += 1
                currentNum += 1
            longest = max(currentLength, longest)
        return longest
