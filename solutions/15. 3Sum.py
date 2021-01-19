class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplet= set()
        
        for i in range(len(nums)-2):
            left = i +1
            right= len(nums)-1
            
            while left < right :
                cursum = nums[i] + nums[left] + nums[right]
                
                if cursum == 0:
                    triplet.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
                elif cursum > 0:
                    right-=1
                else:
                    left+=1
        return triplet
