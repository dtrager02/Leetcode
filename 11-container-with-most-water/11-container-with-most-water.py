class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        l,r = 0,len(height)-1
        while l < r:
            if min((height[l],height[r]))*(r-l) > m:
                m = min((height[l],height[r]))*(r-l)
            if height[l] < height[r]:
                l+= 1
            else:
                r-= 1
        return m