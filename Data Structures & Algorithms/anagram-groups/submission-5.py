"""
b (98) - a (97) = 1
ab

charFreq = [1,1,0,0,0,0,0,0]


[1,1] : ["ab", "ba"]
O(1)

M
N

T: O(M * N)
S: O(G)

Algo:
Create charFreq array
Map charFreq array to list of anagrams
Return list of map values

Input: strs = ["x"]
Output: [["x"]]

["ab", "ba"]
[["ab", "ba"]]

[1,1] 

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        freqToAnagrams = defaultdict(list)
        for word in strs:
            charFreq = [0] * 26
            for letter in word:
                idx = ord(letter) - ord('a')
                charFreq[idx] += 1
            charFreqTuple = tuple(charFreq)
            freqToAnagrams[charFreqTuple].append(word)
        
        return list(freqToAnagrams.values())
        