# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        arr = []
        if not head:
            return True
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr2 = arr[::-1]
        return arr == arr2
