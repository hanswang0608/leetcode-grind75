# implementation with doubly linked list and 2 hashtables
# DLL uses hashtable for O(1) reference to any node
# other hashtable to store cache values
# DLL.head is the least recently used, pop it to retrieve
# whenever a key is used, the corresponding node is moved to end of DLL

class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class DLL:
    
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.table = {}
    
    def insert(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.table[node.key] = node
        
    def pop(self):
        if not self.head:
            return None
        ret = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        if ret == self.tail:
            self.tail = None
        self.table.pop(ret.key)
        return ret
    
    def moveToEnd(self, key):
        if key not in self.table:
            return
        if self.table[key] == self.tail:
            return
        cur = self.table[key]
        prev, next = cur.prev, cur.next
        if cur == self.head:
            self.head = cur.next
        # move cur to end
        cur.prev = self.tail
        cur.next = None
        self.tail.next = cur
        self.tail = cur
        # connect prev and next
        if prev:
            prev.next = next
        next.prev = prev

    def size(self):
        return len(self.table)

    def printDLL(self):
        cur = self.head
        output = ''
        while cur:
            if not cur.prev:
                output += "None "
            output += str(cur.key) + ' '
            if not cur.next:
                output += "None "
            # print(cur.prev.key if cur.prev else None, cur.key, cur.next.key if cur.next else None)
            cur = cur.next
        return output
    

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DLL()
        self.m = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self.dll.moveToEnd(key)        
        return self.m[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.m and self.dll.size() >= self.capacity:
            removed = self.dll.pop()
            self.m.pop(removed.key)
        if key not in self.m:
            self.dll.insert(Node(key))
        self.m[key] = value    
        self.dll.moveToEnd(key)

    def printCache(self):
        print(f"DLL: {self.dll.printDLL()}    Dict: {str(self.m)}")

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(1))
# lRUCache.printCache()
# lRUCache.put(3, 3)
# lRUCache.printCache()

# lRUCache = LRUCache(1)
# lRUCache.put(2, 1)
# print(lRUCache.get(2))
# lRUCache.put(3, 2)
# print(lRUCache.get(2))
# print(lRUCache.get(3))

lRUCache = LRUCache(1)
print(lRUCache.get(6))
print(lRUCache.get(8))
lRUCache.put(12, 1)
print(lRUCache.get(2))
lRUCache.printCache()
lRUCache.put(15, 11)
lRUCache.printCache()
lRUCache.put(5, 2)
lRUCache.put(1, 15)
lRUCache.put(4, 2)
print(lRUCache.get(5))
lRUCache.put(15, 15)


# dll = DLL()
# dll.insert(Node(1))
# dll.insert(Node(2))
# dll.printDLL()
# dll.moveToEnd(1)
# dll.printDLL()
# print(dll.pop().key)
# dll.printDLL()