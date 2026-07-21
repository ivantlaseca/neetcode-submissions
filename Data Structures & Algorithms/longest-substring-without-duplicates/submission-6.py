"""
aaa, 1

l = 1
r = 1
lS: 1
sC: [a]


abca, 3



aAa, 2

"", 0

s="pwwkew", 3

l = 3
r = 5
lS: 3
sC: [k,e,w]

T: O(n) -> Understand why and why not n^2
S: O(n)

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        longestSub = 0
        seenChars = set()
        for r in range(len(s)):
            while s[r] in seenChars:
                seenChars.remove(s[l])
                l += 1
            seenChars.add(s[r])
            longestSub = max(longestSub, r - l + 1)
        return longestSub
        

        