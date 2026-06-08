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
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        maxHeap = []
        output = []
        for key, val in freq.items():
            maxHeap.append([-val, key])
        heapq.heapify(maxHeap)
        
        for i in range(k):
            curr = heapq.heappop(maxHeap)
            output.append(curr[1])
        
        return output


        