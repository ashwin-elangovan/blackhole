class TreeNode:

  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None


def deleteTree(node):
  if node:
    deleteTree(node.left)
    deleteTree(node.right)
    node = None


# Example usage:
if __name__ == "__main__":
  # Constructing a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.left.right = TreeNode(5)

  # Deleting the binary tree
  deleteTree(root)

  # The entire binary tree is now deleted, and root is None
  print(root)  # Output: None
