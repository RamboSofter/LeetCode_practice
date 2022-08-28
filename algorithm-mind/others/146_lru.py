"""
146. LRU 缓存
https://leetcode.cn/problems/lru-cache/
"""


class Node:
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleList:
    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_last(self, x: Node):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def remove_first(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def get_size(self):
        return self.size


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}
        self.cache = DoubleList()

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        self.make_recently(key)
        return self.hash_map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.delete_key(key)
            self.add_recently(key, value)
            return
        if self.cap == self.cache.size:
            self.remove_least_recently()

        self.add_recently(key, value)

    def make_recently(self, key: int):
        x = self.hash_map.get(key)
        self.cache.remove(x)
        self.cache.add_last(x)

    def add_recently(self, key: int, val: int):
        x = Node(key, val)
        self.cache.add_last(x)
        self.hash_map[key] = x

    def delete_key(self, key: int):
        x = self.hash_map.get(key)
        self.cache.remove(x)
        self.hash_map.pop(key)

    def remove_least_recently(self):
        delete_node = self.cache.remove_first()
        delete_key = delete_node.key
        self.hash_map.pop(delete_key)
