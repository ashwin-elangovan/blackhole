class newNode:

  def __init__(self, data):
    self.key = data
    self.left = None
    self.right = None

  # Makes sure str value is printed instead of address
  def __str__(self):
    return str(self.key)


if __name__ == "__main__":
  root = newNode(1)
  root.left = newNode(2)
  root.right = newNode(3)
  root.left.left = newNode(4)
  root.left.right = newNode(5)

  print(root)
