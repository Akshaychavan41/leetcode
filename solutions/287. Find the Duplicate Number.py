class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        
        for x in nums:
            if x in count:
                return x
            else:
                count[x] = 1
        
