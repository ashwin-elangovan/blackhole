from collections import deque

# Binary Tree Node
class newNode:
    # Construct to create a newNode
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def topView(root):
  if not root:
      return []

  top_view = deque()
  queue = deque([(root, 0)])
  top_view.append(root.data)
  
  while queue:
      node, hd = queue.popleft()

      if hd not in top_view:
          if hd < 0:
            top_view.appendleft(node.data)
          else:
            top_view.append(node.data)

      # Enqueue left child with horizontal distance reduced by 1
      if node.left:
          queue.append((node.left, hd - 1))

      # Enqueue right child with horizontal distance increased by 1
      if node.right:
          queue.append((node.right, hd + 1))

  return list(top_view)

# Driver Code
if __name__ == "__main__":

    root = newNode(10)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(8)
    root.right.right = newNode(15)
    root.right.left = newNode(12)
    root.right.right.left = newNode(14)
    print(topView(root))
