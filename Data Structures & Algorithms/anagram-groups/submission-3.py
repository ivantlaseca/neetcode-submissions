"""
Algo
1. Map sorted word to anagrams list
2. Iterate through map and return all values in a list

Input: strs = ["act","cat", "hat"]
Output: [["hat"],["act", "cat"]]


Input: strs = ["x"]
Output: [["x"]]

Input: strs = [""]
Output: [[""]]

"""

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        
        anagrams = {}
        for word in strs:
            sortedWord = sorted(word)
            sortedWord = "".join(sortedWord)
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
            