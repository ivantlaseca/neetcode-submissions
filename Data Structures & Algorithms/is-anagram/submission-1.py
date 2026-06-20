"""
avc
aab

a : 0
v : 1
c : 1

False

aba
baa

a : 0
b : 0




If size of strings isn't equal, return false

Iterate through s, mapping the freq of each char to the char
Iterate through t
    If character doesn't already exist in map or val of char in map is <= 0, return false
    Reduce val of current char by 1
Iterate through values in the map, if all values are 0 return true

"""

class Solution:

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        charToFreq = {}
        for c in s:
            charToFreq[c] = charToFreq.get(c, 0) + 1
        
        for c in t:
            if c not in charToFreq or charToFreq[c] <= 0:
                return False
            charToFreq[c] -= 1
        
        for x in charToFreq.values():
            if x != 0:
                return False
        return True