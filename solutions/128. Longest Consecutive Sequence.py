class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dic = {}
        if not nums:
            return 0
        for x in nums:
            dic[x] =  True
        maxL = 1
        for x in nums :
            if not dic[x]:
                continue
            l = 1
            dic[x] = False
            left = x-1
            right = x+1
            while left in dic:
                dic[left] = False
                l+=1
                left-=1
                
            while right in dic:
                dic[right] = False
                l+=1
                right+=1
                
            maxL = max(maxL, l)
        
        return maxL
            
