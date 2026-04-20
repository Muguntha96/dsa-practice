# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

#     LRUCache(int capacity) Initialize the LRU cache of size capacity.
#     int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in O(1)O(1) average time complexity.

# Example 1:

# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20 
# lRUCache.get(1);      // return -1 (not found)

class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:
    def __init__(self,capacity:int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
    def insert(self,node):
        prev=self.right.prev
        nxt=self.right

        prev.next=node
        node.prev=prev

        node.next=nxt
        nxt.prev=node
        
    def remove(self,node):
        prev=node.prev
        nxt=node.next

        prev.next=nxt
        nxt.prev=prev
    def get(self,key:int)->int:
        if key not in self.cache:
            return "null"
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
    def put(self,key:int,value:int)->None:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            node.val=value
            self.insert(node)
            return
        if len(self.cache)>=self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        node=Node(key,value)
        self.cache[key]=node
        self.insert(node)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))   # 10

cache.put(3, 30)      # removes key 2

print(cache.get(2))   # -1

cache.put(4, 40)      # removes key 1

print(cache.get(1))   # -1
print(cache.get(3))   # 30
print(cache.get(4))   # 40

    