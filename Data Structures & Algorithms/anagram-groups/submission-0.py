class Solution:
    """
    ["act","pots","tops","cat"]
    out: [["act", "cat"], ["pots", "tops"]]


    charToString = 
    {
    [1,0,1,0,0...,1] : ["act", "cat"]
    }

    [1,0,0,0,0]

    Iterate through IN
    Take frequency of each element in IN
    Append element to charToString if we have a key already, else create a key and append to the list
    Return the values of charToString

    strs: ["act","pots","tops","cat"]
    out: [["act", "cat"], ["pots", "tops"]]

    act

    charToString = 
    {
    [1,0,1,...,1] : ["act"],
    [0,0,0,...,0] : ["pots"]
    }

    freq = [0,0,0,...,0]




    """
    # O(n * m)
    # O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charToString = defaultdict(list)
        # Iterate through the words
        # O(n)
        for word in strs:
            frequencies = [0] * 26 # Learn how to explain this part better
            # Iterate through each char and count the frequencies
            # O(m)
            for letter in word:
                c = (ord(letter) - ord('a'))  # Learn how to explain this part better
                frequencies[c] += 1
            # Map the word to the frequency list/array
            charToString[tuple(frequencies)].append(word)
        
        return list(charToString.values())

