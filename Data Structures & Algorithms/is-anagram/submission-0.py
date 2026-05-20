class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
                if letters[letter] == 0:
                    del letters[letter]

        return len(letters) == 0