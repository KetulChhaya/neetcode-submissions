"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNewMap = {}
        ptr = head
        while ptr:
            newNode = Node(ptr.val)
            oldToNewMap[ptr] = newNode
            ptr = ptr.next
        
        ptr = head
        while ptr:
            newNode = oldToNewMap[ptr]
            newNode.next = oldToNewMap[ptr.next] if ptr.next else None
            newNode.random = oldToNewMap[ptr.random] if ptr.random else None
            ptr = ptr.next
        
        return oldToNewMap[head] if head else None