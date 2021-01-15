class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = {}
        r = []
        if nums1 is None or nums2 is None:
            return []
        for x in nums1:
            if x in c:
                c[x]+=1
            else:
                c[x] =1
        
        for y in nums2:
            if y in c and c[y]>0:
                r.append(y)
                c[y]-=1
        
        return r
