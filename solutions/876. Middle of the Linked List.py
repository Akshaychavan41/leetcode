# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #count number of nodes
        
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        nxt = count//2 +1
        count = 1
        curr = head
        while count < nxt:
            count+=1
            curr= curr.next
        return curr
        
