"""
1. Count freq of each num in array
2. Sort the values, return the top k keys
O(m * n log n)



"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for num in nums:
            numToFreq[num] = numToFreq.get(num, 0) + 1
        j = 0
        out = []
        while j < k:
            mostFreq = max(numToFreq, key=numToFreq.get)
            numToFreq.pop(mostFreq)
            out.append(mostFreq)
            j += 1
        return out

        