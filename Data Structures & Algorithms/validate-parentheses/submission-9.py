class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {')' : '(', ']' : '[', '}': '{'}

        for char in s:
            if char in "[({":
                stack.append(char)
            elif char in "]})" :
                if stack and stack[-1] == pairs[char]:
                    stack.pop(len(stack) - 1)
                else:
                    return False
        
        return len(stack) == 0 


     