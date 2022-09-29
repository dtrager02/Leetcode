from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        chars,window = defaultdict(int),defaultdict(int)
        for char in s1:
            chars[char] += 1
        counter = 0
        l,r = 0,0
        # for i in range(0,len(s2)):
        #     if s2[i] in chars and window[s2[i]] < chars[s2[i]]:
        #         window[s2[i]]+=1
        #     else:
        #         window = defaultdict(int)
        #         l = i+1
        while r < len(s2):
            window[s2[r]]+=1
            if s2[r] in chars and window[s2[r]] <= chars[s2[r]]:
                if r-l == len(s1)-1:
                    return True
            elif s2[r] in chars:
                while window[s2[r]] > chars[s2[r]]:
                    window[s2[l]] -=1
                    l+=1
            else:
                while l <=r:
                    window[s2[l]] -=1
                    l+=1
            r+=1
        return False