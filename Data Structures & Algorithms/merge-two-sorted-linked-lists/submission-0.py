# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        if not list1 or not list2:
            return list1 if list1 else list2
    
        ptr1, ptr2 = list1, list2
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                curr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            curr = curr.next
        
        if ptr1:
            curr.next = ptr1
        if ptr2:
            curr.next = ptr2
        
        return dummy.next
