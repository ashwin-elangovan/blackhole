class TreeNode:

  def __init__(self, key):
    self.value = key
    self.left = None
    self.right = None


def size_of_the_tree(root):
  if not root:
    return 0
  return size_of_the_tree(root.left) + 1 + size_of_the_tree(root.right)


# Example usage:
if __name__ == "__main__":
  # Constructing a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(3)

  # Size of the binary tree
  print(size_of_the_tree(root))
