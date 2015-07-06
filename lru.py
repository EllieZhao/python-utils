class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.l = []
        self.v = {}
        
    # @return an integer
    def get(self, key):
        if key in self.l:
            self.l.remove(key)
            self.l.append(key)
            return self.v[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.l:
            self.l.remove(key)
        self.l.append(key)
        self.v[key] = value
        if len(self.l) > self.capacity:
            del self.v[self.l[0]]
            self.l.remove(self.l[0])

lru = LRUCache(2)
lru.set(2,1)
lru.set(1,1)
print lru.get(2)
lru.set(4,1)
print lru.get(1)
print lru.get(2)
