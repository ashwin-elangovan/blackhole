class TreeNode:
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None

def inorder_successor(root):
  current = root
  while current.left is not None:
      current = current.left
  return current

def delete_node(root, key):
  if root is None:
      return root

  if key < root.key:
      root.left = delete_node(root.left, key)
  elif key > root.key:
      root.right = delete_node(root.right, key)
  else: # is root.key is equal to the expected value
      if root.left is None:
          temp = root.right
          root = None
          return temp
      elif root.right is None:
          temp = root.left
          root = None
          return temp

      temp = inorder_successor(root.right)
      root.key = temp.key
      root.right = delete_node(root.right, temp.key)

  return root

def inorder_traversal(root):
  if root:
      inorder_traversal(root.left)
      print(root.key, end=" ")
      inorder_traversal(root.right)

# Example usage:
if __name__ == "__main__":
  root = TreeNode(50)
  root.left = TreeNode(30)
  root.right = TreeNode(70)
  root.left.left = TreeNode(20)
  root.left.right = TreeNode(40)
  root.right.left = TreeNode(60)
  root.right.right = TreeNode(80)

  print("Inorder traversal before deletion:")
  inorder_traversal(root)
  print("\n")

  key_to_delete = 30
  root = delete_node(root, key_to_delete)

  print(f"After deleting node with key {key_to_delete}:")
  inorder_traversal(root)
