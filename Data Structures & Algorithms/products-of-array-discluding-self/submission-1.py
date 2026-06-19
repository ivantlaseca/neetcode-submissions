"""
[2,4]
   i



left: [1,2]
right: [4,1]

out: [4,2]

l : [1,2]
r : [4,1]
o : [4,2]

"""

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        left, right, out = [0] * n, [0] * n, [0] * n
        left[0] = 1
        right[n - 1] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * arr[i - 1]
        for j in range(n - 2, -1, -1):
            right[j] = right[j + 1] * arr[j + 1]
        for x in range(n):
            out[x] = left[x] * right[x]
        return out