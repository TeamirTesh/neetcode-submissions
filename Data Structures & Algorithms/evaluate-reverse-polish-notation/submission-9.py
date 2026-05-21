class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        t = 0

        for char in tokens:
            if char not in operators:
                stack.append(int(char))
                t += 1
            else:
                if char == '+':
                    val = stack[t-2] + stack[t-1]
                elif char == '-':
                    val = stack[t-2] - stack[t-1]
                elif char == '*':
                    val = stack[t-2] * stack[t-1]
                elif char == '/':
                    val = int(stack[t-2] / stack[t-1])
                
                if t > 1:
                    stack = stack[0:t-2] + [val]
                else:
                    stack = [val]
                
                t -= 1

        return stack[0]