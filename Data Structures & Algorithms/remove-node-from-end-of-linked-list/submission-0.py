# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        ptr = head
        while ptr:
            N += 1
            ptr = ptr.next
        
        removeInd = N - n
        if N-n ==0:
            return head.next
        
        ptr = head
        i=0
        while ptr:
            if (i+1) == removeInd:
                ptr.next = ptr.next.next
            i += 1
            ptr = ptr.next

        return head 