class TreeNode:

  def __init__(self, key):
    self.value = key
    self.left = None
    self.right = None


def level_order_traversal(root):
  if not root:
    return
  q = [root]
  while q:
    temp = q.pop(0)
    print(temp.value)
    if temp.left:
      q.append(temp.left)
    if temp.right:
      q.append(temp.right)
  return root


# Example usage:
if __name__ == "__main__":
  # Constructing a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(3)

  # Deleting the binary tree
  level_order_traversal(root)

  # The entire binary tree is now deleted, and root is None
  print(root)  # Output: None
