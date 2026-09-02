class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = Counter(nums)
        kElements = []
        out = []

        for num, freq in numToFreq.items():
            curr = (freq, num)
            heapq.heappush(kElements, curr)
            if len(kElements) > k:
                heapq.heappop(kElements)
        
        while kElements:
            curr = heapq.heappop(kElements)[1]
            out.append(curr)
        
        return out





        