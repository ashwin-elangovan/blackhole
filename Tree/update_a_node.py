class NewNode:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def update_node(root, find_val, replace_value):
    if not root:
      return

    q = [root]

    while q:
      temp = q.pop(0)
      if temp.value == find_val:
        temp.value = replace_value
        return

      if root.left:
        q.append(root.left)
      if root.right:
        q.append(root.right)


root = NewNode(1)
root.left = NewNode(3)
print(root.left.value)

root.update_node(3, 5)
print(root.left.value)
