from collections import deque

# using an increasing id var to tag each get/put access and push onto a queue
# keep another dict to store the valid id for every key
# when cache at capacity limit, pop queue until a valid id is found (this is least recently used key) and pop it
# time complexity: O(1) get, O(1) put except for limit, then I think it's O(# of gets)
# space complexity: O(n) where n is # of get/put calls because each call appends an access history to the queue
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}     
        self.capacity = capacity   
        self.history = deque()
        self.recent = {}
        self.id = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.history.append((key, self.id))
            self.recent[key] = self.id
            self.id += 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            accessedKey, accessID = self.history.popleft()
            while self.history and accessID != self.recent[accessedKey]:
                accessedKey, accessID = self.history.popleft()
            self.cache.pop(accessedKey)
        self.cache[key] = value
        self.history.append((key, self.id))
        self.recent[key] = self.id
        self.id += 1

    def printCache(self):
        print(self.cache, self.history)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.printCache()
lRUCache.put(3, 3)
lRUCache.printCache()