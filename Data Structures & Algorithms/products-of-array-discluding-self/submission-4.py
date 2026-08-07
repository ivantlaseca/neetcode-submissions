"""
123
112
631

632
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = [0] * n, [0] * n
        pre[0], post[n-1] = 1, 1

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        out = [0] * n
        for i in range(n):
            out[i] = pre[i] * post[i]
        
        return out
        
        
