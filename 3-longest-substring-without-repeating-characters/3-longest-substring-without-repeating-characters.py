class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(set(s))
        l,r = 0,1
        tracker = set([s[0]])
        maxlen = 1
        while r < len(s):
            # print(tracker)
            if s[r] in tracker:
                while s[l] != s[r]:
                    tracker.remove(s[l])
                    l += 1
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            maxlen = max((maxlen,len(tracker)))
            r += 1
        return maxlen