"""

[4,4,2] k = 2

4 : 2
2 : 1

[[],[2],[4]]
  0  1  2

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = defaultdict(int)
        for num in nums:
            numToFreq[num] += 1
        
        frequencies = [[] for _ in range(len(nums) + 1)]
        for num, freq in numToFreq.items():
            frequencies[freq].append(num)
        
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res
        


        