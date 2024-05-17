# fix this

class Node:
  def __init__(self, data):
      self.data = data
      self.prev = None
      self.next = None

class Stream:
  def __init__(self):
      self.head = None
      self.tail = None
      self.middle = None
      self.size = 0

  def insert_start(self, data):
      new_node = Node(data)
      if self.head is None:
          self.head = new_node
          self.tail = new_node
          self.middle = new_node
      else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
          if self.size % 2 == 0:
              self.middle = self.middle.prev
      self.size += 1

  def insert_end(self, data):
      new_node = Node(data)
      if self.tail is None:
          self.head = new_node
          self.tail = new_node
          self.middle = new_node
      else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node
          if self.size % 2 == 1:
              self.middle = self.middle.next
      self.size += 1

  def insert_middle(self, data):
      new_node = Node(data)
      if self.middle is None:
          self.head = new_node
          self.tail = new_node
          self.middle = new_node
      else:
          new_node.prev = self.middle
          new_node.next = self.middle.next
          if self.middle.next:
              self.middle.next.prev = new_node
          self.middle.next = new_node
          if self.size % 2 == 0:
              self.middle = self.middle.next
      self.size += 1

  def delete_start(self):
      if self.head is None:
          return None
      data = self.head.data
      if self.head == self.middle:
          self.middle = self.middle.next
      if self.head.next:
          self.head = self.head.next
          self.head.prev = None
      else:
          self.head = None
          self.tail = None
          self.middle = None
      self.size -= 1
      return data

  def delete_end(self):
      if self.tail is None:
          return None
      data = self.tail.data
      if self.tail == self.middle:
          self.middle = self.middle.prev
      if self.tail.prev:
          self.tail = self.tail.prev
          self.tail.next = None
      else:
          self.head = None
          self.tail = None
          self.middle = None
      self.size -= 1
      return data

  def get_middle(self):
      if self.middle:
          return self.middle.data
      else:
          return None

# Example usage:
stream = Stream()
stream.insert_start(1)
stream.insert_end(3)
stream.insert_middle(2)
print("Middle element:", stream.get_middle())  # Output: 2
stream.insert_start(0)
print("Middle element:", stream.get_middle())  # Output: 1
stream.delete_end()
print("Middle element:", stream.get_middle())  # Output: 1
