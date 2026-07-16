class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Failure cases
        if k > len(nums):
            return []

        nToF = defaultdict(int)
        for num in nums:
            nToF[num] += 1

        output = []

        for i in range(k):
            mostFreq = max(nToF, key=nToF.get) # O(n)
            output.append(mostFreq)       
            del nToF[mostFreq]
        
        return output




            


        