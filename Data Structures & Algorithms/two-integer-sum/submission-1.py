class Solution:
    """
    nums = [3,4,5,6], target = 7

    map: 3 -> 0, 4 -> 1,5,6
    7 - 3 = 4

    Output: [0,1]



    """


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for p1 in range(len(nums)):
            for p2 in range(p1 + 1, len(nums)):
                if nums[p1] + nums[p2] == target:
                    return [p1,p2]

        return [0,0]


        