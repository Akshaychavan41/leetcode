class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        return self.quick_select(nums, k, 0, len(nums) - 1)
​
# Option1: find kth largest number between left and right.
    def quick_select(self, nums, k, start, end):
        l, r = start, end
        mid = l + (r - l) // 2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
​
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if start + k - 1 <= r:
            return self.quick_select(nums, k, start, r)
        if start + k - 1 >= l:
            return self.quick_select(nums, k - (l - start), l, end)
        return nums[r + 1]
