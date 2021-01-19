class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for x, v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v], x]
            else:
                dic[v] = x
