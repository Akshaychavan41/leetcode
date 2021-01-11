class Solution:
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permuteHelper(0, nums, permutations)
        
        return permutations
    
            
    def swap(self,arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    def permuteHelper(self, i, nums, perms):
        
        if i == len(nums) -1 :
            perms.append(nums[:])
        else:
            for j in range(i,len(nums)):
                self.swap(nums, i, j)
                self.permuteHelper(i+1, nums, perms)
                self.swap(nums, i, j)
    
​
