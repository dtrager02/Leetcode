from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        for i in range(len(out)):
            while len(stack) and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                out[temp] = i - temp
            stack.append(i)
        return out
            
            