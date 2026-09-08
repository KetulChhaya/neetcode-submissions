# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

            if len(stack) == k:
                while stack:
                    tail.next = stack.pop()
                    tail = tail.next
        
        while stack:
            tail.next = stack.pop(0) #stack.pop(0) preserves the original order
            tail = tail.next
        tail.next = None

        return dummy.next
                