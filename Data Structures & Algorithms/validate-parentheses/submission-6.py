"""
} : {
] : 
)

(}, false

Algo:
Map closeToOpen
Iterate s, appending opening parentheses to stack and checking if closing parentheses correspond to top of stack

{}, true

{), false

[(}], false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        closeToOpen = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        openParentheses = []

        for c in s:
            isClosingBracket = c in closeToOpen
            if isClosingBracket:
                if openParentheses and closeToOpen[c] == openParentheses[-1]:
                    openParentheses.pop()
                else:
                    return False
            else:
                openParentheses.append(c)
        
        return True if not openParentheses else False
                
                    
        