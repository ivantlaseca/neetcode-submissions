class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf, out = [0] * n, [0] * n, [0] * n
        pre[0], suf[n-1] = 1, 1
        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        for i in range(len(out)):
            out[i] = pre[i] * suf[i]
        return out

        