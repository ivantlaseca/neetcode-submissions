"""
Count frequency of all elements in nums, store in map
Heapify this map
Return top k elements from heap in a list

1 : 1
2 : 2
3 : 3

(1,1)
(2,2)
(3,3)

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = defaultdict(int)
        for num in nums:
            numToFreq[num] += 1
        
        heap = []
        for key, val in numToFreq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = []
        for _ in range(k):
            out.append(heapq.heappop(heap)[1])
        
        return out


        

        