class Solution:
    """
    nums (int) 
    true if any val (x) appears more than once in the array

    Notes:
    - return bool
    - only ints are passed into nums

    A1: HashSet 

    ex: [1,2,3,4,2] true

    elements: (1,2,3,4)



    set: (1,2,3,4)
    if element exists already, return true

    return false


    ex: [9] false

    elements: (9)

    ex: [] false
    Q: What do we return for an empty array?

    ex: [1,2,3] 
    elements: (1,2,3)

    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <=1:
            return False
        elements = set()
        for num in nums:
            if num in elements:
                return True
            elements.add(num)

        return False
        