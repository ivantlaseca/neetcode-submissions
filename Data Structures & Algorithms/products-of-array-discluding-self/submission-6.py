


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [0] * len(nums), [0] * len(nums)
        pre[0], post[len(nums) - 1] = 1, 1
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        
        out = [0] * len(nums)

        for i in range(len(nums)):
            out[i] = pre[i] * post[i]
        
        return out

        