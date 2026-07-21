"""
T: O(n^2), S: O(n)

abcde, 4

aab, 2

aA, 2

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0, 1
        maxSub = 0
        while i < len(s):
            seenChars = set()
            seenChars.add(s[i])
            while j < len(s):
                if s[j] in seenChars:
                    break
                seenChars.add(s[j])
                j += 1
            i += 1
            j = i + 1
            maxSub = max(maxSub, len(seenChars))
        return maxSub

        