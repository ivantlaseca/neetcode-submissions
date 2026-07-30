"""
map the closing brackets to opening brackets
iterate through the string, appending opening brackets to a stack
when we see a closing bracket, check the top of our stack for the corresponding opening bracket.
if corresponding, pop and continue, else return false

T: O(n)
S: O(n)

[()], T

s: 


[{], F


[, F

], F

"""

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        openingBrackets = []

        for bracket in s:
            isClosingBracket = bracket in closeToOpen

            if isClosingBracket:
                if not openingBrackets:
                    return False
                if closeToOpen[bracket] != openingBrackets[-1]:
                    return False
                openingBrackets.pop()
            else:
                openingBrackets.append(bracket)
        
        return len(openingBrackets) == 0
