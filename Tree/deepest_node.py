class TreeNode:

  def __init__(self, key):
    self.value = key
    self.left = None
    self.right = None


def deepest_node(root):
  if not root:
    return
  q = [root]
  temp = None
  while q:
    temp = q.pop(0)
    if temp.left:
      q.append(temp.left)
    if temp.right:
      q.append(temp.right)
  return temp


# Example usage:
if __name__ == "__main__":
  # Constructing a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(5)

  # deepest_node of the binary tree
  print(deepest_node(root).value)
