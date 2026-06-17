"""
How are we delimitting the strings? 
Since strs[i] can have any possible char of the 256 ASCII characters, a naive soln. uses non-ascii chars for delimitting. What's a better way?
How big/small can this list of strings be?
What kinds of characters can we expect in this list of strings?
If commas are ASCII characters, how else can we delimit the characters of the string?
Can there be duplicate strings in the list?
What is the rule for the casing of the strings in the list?
Does the ordering of the output matter?


4#neet#5co#de

append length + # to string and then the word itself

str[j + 1 : j + 1 + length]
str[charAfterHash : charsAtLengthOfWord]

"""

class Solution:

    def encode(self, strs: list[str]):
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr
    
    def decode(self, encodedStr: str):
        decodedStr = []
        i = 0
        while i < len(encodedStr):
            j = i
            while encodedStr[j] != "#":
                j += 1
            lengthOfWord = int(encodedStr[i:j])
            charAfterHash = j + 1
            decodedStr.append(encodedStr[j + 1 : j + 1 + lengthOfWord])
            i = j + 1 + lengthOfWord
        return decodedStr