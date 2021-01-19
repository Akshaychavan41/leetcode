class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        if not nums:
            return 0
        
        maxL = 1
        currL = 1
        
        for x in range(1,len(nums)):
            if nums[x] - nums[x-1] == 1:
                currL+=1
                maxL = max(currL,maxL)
            elif nums[x] == nums[x-1]:
                continue
            else:
                currL = 1
        return maxL
