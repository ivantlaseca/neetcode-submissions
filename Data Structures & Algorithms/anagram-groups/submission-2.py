"""
Map each sorted string to all of it's anagrams and return a list of all values in our map.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagrams = {}
        for word in strs:
            sortedWord = sorted(word)
            sortedWord = ''.join(sortedWord)
            if sortedWord not in anagrams:
                anagrams[sortedWord] = []
            anagrams.get(sortedWord).append(word)

        groupedAnagrams = []

        for group in anagrams.values():
            groupedAnagrams.append(group)

        return groupedAnagrams        