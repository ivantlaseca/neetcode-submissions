class Solution:
    """
    nums = [3,4,5,6], target = 7

    7 - 4 = 3
    map: 3 -> 0, 

    out: [0,1]

    nums = [5,5], target = 10

    10 - 5 = 5

    map: 5 -> 0

    output: [0,1]



    """


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indx, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], indx]
            seen[num] = indx




        