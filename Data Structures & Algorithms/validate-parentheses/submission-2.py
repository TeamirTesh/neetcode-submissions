class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        stack = []

        for letter in s:
            if letter in matches:
                if len(stack) == 0 or matches[letter] != stack.pop():
                    return False
            
            else:
                stack.append(letter)

        return len(stack) == 0
                