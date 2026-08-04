"""
Expanding our window, using two ptrs
Keeping track of the size of the substring
Keeping track of the characters in the substring

How big/small is the input?
T/S constraints?
*What kinds of chars are in s?

Improvement: Think outside the box for questions.

T: O(n)
S: O(n)

1. Iterate through s, nested loops
2. Add/remove characters from set, depending on if they already exist in the substring
a. Move pointers, and pop from set accordingly (if character is already in the set)
3. Calculate maxSubstringSize
4. return maxSubstringSize

Improvement: Work on getting this algo written more clearly

Tests:

"abc", 3
ss: a, b, c
mS: 3

* Current code will check for the maxSubstring, starting from every single character (outer for-loop). How do we prevent that?

"abab", 2
ss: a, b
mS: 2

"", 0

"aaa", 1

"""
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        substring = set()
        maxSubstringSize = 0
        i = 0
        for j in range(len(s)):
            while s[j] in substring:
                substring.remove(s[i])
                i += 1
            substring.add(s[j])
            maxSubstringSize = max(len(substring), maxSubstringSize)
        
        return maxSubstringSize
                

