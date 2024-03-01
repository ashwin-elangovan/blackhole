class NewNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.value)

  def add_node(self, root, value):
    if not root:
      return NewNode(value)

    q = []
    q.append(root)

    while q:
      node = q.pop(0)

      if node.left:
        q.append(node.left)
      else:
        node.left = NewNode(value)
        return

      if node.right:
        q.append(root.right)
      else:
        node.right = NewNode(value)
        return


root = NewNode(1)
root.add_node(root, 2)

print(root)
print(root.left)
print(root.right)
