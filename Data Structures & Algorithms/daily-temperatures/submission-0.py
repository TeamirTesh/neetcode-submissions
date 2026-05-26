class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair [temp, index]
    
        for i in range(len(temperatures) - 1):
            stack.append([temperatures[i], i])

            while stack and temperatures[i+1] > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1] + 1
                stack.pop()

        return res