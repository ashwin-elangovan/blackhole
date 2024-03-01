class Node:

  def __init__(self, key):
    self.left = None
    self.right = None
    self.value = key

  def printInorder(self, root):
    if root:
      self.printInorder(root.left)
      print(root.value, end=" "),
      self.printInorder(root.right)

  # parent of the rightmost node
  def delete_node(self, root, value):
    if not root:
      return
    q = [root]
    node_to_be_deleted = None
    parent_node = None
    temp = None
    while q:
      temp = q.pop(0)
      if temp.value == value:
        node_to_be_deleted = temp
      if temp.left:
        parent_node = temp
        q.append(temp.left)
      if temp.right:
        parent_node = temp
        q.append(temp.right)

    if node_to_be_deleted:
      node_to_be_deleted.value = temp.value
      if parent_node.right:
        parent_node.right = None
      else:
        parent_node.left = None
    return root


# Driver code
if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

  # Function call
  root.printInorder(root)
  print("")
  root.delete_node(root, 3)
  print("")
  print(root)
  root.printInorder(root)
