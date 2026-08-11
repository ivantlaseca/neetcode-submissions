"""
aba
2



"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()
        left = 0
        longestSub = 1
        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            longestSub = max(longestSub, len(seen))
        return longestSub

