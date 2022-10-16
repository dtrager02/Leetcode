from collections import deque
class Solution:
    def numTrees(self, n: int) -> int:
        g = [0 for i in range(n+1)]
        g[0],g[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,i+1):
                g[i] += g[i-j]*g[j-1]
        return g[n]
            