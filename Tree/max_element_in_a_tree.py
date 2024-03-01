class TreeNode:

  def __init__(self, key):
    self.value = key
    self.left = None
    self.right = None


def max_element(root):
  if not root:
    return float('-inf')
  lmax = max_element(root.left)
  rmax = max_element(root.right)
  return max(root.value, lmax, rmax)


# Example usage:
if __name__ == "__main__":
  # Constructing a binary tree
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(2)
  root.left.left = TreeNode(3)
  root.left.right = TreeNode(3)

  # Size of the binary tree
  print(max_element(root))
