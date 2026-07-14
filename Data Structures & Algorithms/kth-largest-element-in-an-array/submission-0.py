class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kLargest = []
        for n in nums:
            if len(kLargest) < k:
                heapq.heappush(kLargest, n)
            elif n > kLargest[0]:
                heapq.heapreplace(kLargest, n)
        
        return kLargest[0]
        