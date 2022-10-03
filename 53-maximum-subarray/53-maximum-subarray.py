class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = nums[0]
        currsum = 0
        for num in nums:
            s = max((0,currsum))
            currsum = s + num
            currmax = max((currmax,currsum))
        return currmax
            
            