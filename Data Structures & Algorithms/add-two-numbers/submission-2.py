# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        carry = 0
        dummy = ListNode()
        tail = dummy
        while ptr1 or ptr2 or carry:
            num1 = ptr1.val if ptr1 else 0
            num2 = ptr2.val if ptr2 else 0
            
            summ = num1 + num2 + carry
            carry = summ // 10

            tail.next = ListNode(summ%10)
            tail = tail.next
            
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        return dummy.next
