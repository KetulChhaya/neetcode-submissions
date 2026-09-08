class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #hashmap of key and node (key, val)
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        tmp = self.right.prev
        node.prev = tmp
        tmp.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
