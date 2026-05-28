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
        numToIndx = {}
        smallerIndx = 0
        largerIndx = 0
        for p1 in range(len(nums)):
            diff = target - nums[p1]
            if diff in numToIndx:
                smallerIndx = p1 if numToIndx[diff] > p1 else numToIndx[diff]
                largerIndx = numToIndx[diff] if numToIndx[diff] > p1 else p1
            else:
                numToIndx[nums[p1]] = p1
        
        return [smallerIndx, largerIndx]



        