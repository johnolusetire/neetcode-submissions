# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse 2nd half of list
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        l1, l2 = head, prev

        while l1:
            tmp = l1.next
            l1.next = l2
            l1 = tmp
            
            if l2:
                tmp = l2.next
                l2.next = l1
                l2 = tmp
        return


        