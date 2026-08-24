"""
Algo
Iterate strs
Create a list to count freq of each char
Map freq to anagrams
Return list of grouped anagrams

a - a
97 - 97 = 0
b - a
98 - 97 = 1

[0,0,0,...,0]

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToAnagrams = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            key = tuple(freq)
            freqToAnagrams[key].append(word)
        
        return list(freqToAnagrams.values())
            

        