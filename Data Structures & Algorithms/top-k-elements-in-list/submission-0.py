class Solution:
    """
    [1,2,2,3,3,3] k = 2

    1 : 1
    2 : 2
    3 : 3

    [2,3]

    [7] k = 1

    nTF = { }
    topK = [7]

    [1,1,2,2] k = 1

    [1,2,3,3] k = 2

    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nToFreq = {}
        topK = []
        # Count frequencies of each integer
        for n in nums:
            nToFreq[n] = nToFreq.get(n, 0) + 1
        
        for _ in range(k):
            mostFrequentNum = max(nToFreq, key=nToFreq.get)
            nToFreq.pop(mostFrequentNum)
            topK.append(mostFrequentNum)
        return topK


        