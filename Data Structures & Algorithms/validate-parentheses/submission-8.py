class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        openParentheses = []
        for p in s:
            if p in closeToOpen:
                if openParentheses and openParentheses[-1] == closeToOpen[p]:
                    openParentheses.pop()
                else:
                    return False
            else:
                openParentheses.append(p)
        
        return True if not openParentheses else False
        
        