class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def diameter(root):
  res = [0]

  def dfs(root):
    if root is None:
      return -1
    left = dfs(root.left)
    right = dfs(root.right)
    res[0] = max(res[0], 2 + left + right)

    return 1 + max(left, right)

  dfs(root)
  return res[0]


def insert(root, value):
  if root is None:
    return Node(value)
  else:
    if value == root.data:
      return root
    elif value < root.data:
      root.left = insert(root.left, value)
    elif value > root.data:
      root.right = insert(root.right, value)
  return root


def search(root, key):
  if root is None or root.data == key:
    return root
  else:
    if key < root.data:
      return search(root.left, key)
    elif key > root.data:
      return search(root.right, key)


def minValue(root):
  if root.left is None:
    return root
  return minValue(root.left)


def maxValue(root):
  if root.right is None:
    return root

  return minValue(root.right)

def deleteNode(key, root):
  if root is None:
    return root

  if key < root.data:
    root.left = deleteNode(root.left, key)

  elif key > root.data:
    root.right = deleteNode(root.right, key)

  else:
    # Single children case
    if root.left is None:
      temp = root.right
      root = None
      return temp

    if root.right is None:
      temp = root.left
      root = None
      return temp

    # Multi children case
      temp = minValue(root.right)
      root.key = temp.key
      deleteNode(temp.key, root.right)


root = Node(50)
root = insert(root, 25)
root = insert(root, 15)
root = insert(root, 20)

print(search(root, 25).data)
print(minValue(root).data)
print(maxValue(root).data)
print(diameter(root))
