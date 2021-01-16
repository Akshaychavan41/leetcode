class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1,p2 = 0, len(nums)-1
        p = 0
        
        while p <= p2:
            val = nums[p]
            
            if val == 0:
                nums[p] , nums[p1] = nums[p1], nums[p]
                p+=1
                p1+=1
            elif val ==2:
                nums[p] , nums[p2] = nums[p2], nums[p]
                p2-=1
            else:
                p+=1
