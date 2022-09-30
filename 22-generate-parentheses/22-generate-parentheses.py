from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = deque([[")",0,1]])
        i = 1
        while i < 2*n:
            b = len(a)
            temp = 0
            while temp < b:
                item = a.popleft()
                item2 = item.copy()
                if item[2] > item[1]:
                    item[0] = "("+item[0]
                    item[1]+=1
                    a.append(item)
                    
                if item2[2] < n:
                    item2[0] = ")"+item2[0]
                    item2[2]+=1
                    a.append(item2)
                temp += 1
            i+=1
        return [a.pop()[0] for _ in range(len(a))]