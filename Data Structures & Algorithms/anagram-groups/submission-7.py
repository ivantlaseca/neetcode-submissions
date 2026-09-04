class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToAnagrams = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            sortedToAnagrams[sortedWord].append(word)
        
        groupedAnagrams = []
        for sortedWord, anagrams in sortedToAnagrams.items():
            groupedAnagrams.append(anagrams)
        
        return groupedAnagrams


        