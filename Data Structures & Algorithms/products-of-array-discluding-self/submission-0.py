"""
Negatives? Yes
Guaranteed to fit in a 32-bit integer (what's that mean for the soln.?)
Range of values of the elements in nums?
Size of nums?

nums = [1,2,4,6]
       p1 p2

[0,1,2]
       i
       j
output = [2,0,0]
exp = [2,0,0]
product = 0

[-1,20,2]

[1,5,10]


Two pointers

Iterate through nums
    Iterate through all elements except the current one from the outer loop
        Take the product of these elements
        Append the product to our output array
Return output


"""

class Solution:

    def productExceptSelf(self, nums):
        arr = nums
        out, i = [], 0
        while i < len(arr):
            j = 0
            product = 1
            while j < len(arr):
                if j == i:
                    j += 1
                if j == len(arr):
                    break
                product *= arr[j]
                j += 1
            out.append(product)
            i += 1
        return out
                


