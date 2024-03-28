class Node:

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev, self.next = None, None


class LRUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.keys = {}

    # To maintain order we are going with a doubly linked list
    # Left is least common and right is most common
    self.left, self.right = Node(0, 0), Node(0, 0)
    self.left.next, self.right.prev = self.right, self.left

  # Insert in the rightmost point
  def insert(self, node):
    prev, next = self.right.prev, self.right
    # Linking others to node
    prev.next = node
    next.prev = node
    # Linking node to others
    node.next = next
    node.prev = prev

  # Delete from the linked list
  def remove(self, node):
    prev, next = node.prev, node.next
    prev.next = next
    next.prev = prev

  def get(self, key: int) -> int:
    if key in self.keys:
      # Add the node to the right and delete the node from the previous place
      self.remove(self.keys[key])
      self.insert(self.keys[key])
      return self.keys[key].value
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.keys:
      self.remove(self.keys[key])
    self.keys[key] = Node(key, value)
    self.insert(self.keys[key])

    if len(self.keys) > self.capacity:
      # If the cache capacity exceeds, remove the least recently used node (LRU)
      lru = self.left.next
      self.remove(lru)
      del self.keys[lru.key]
