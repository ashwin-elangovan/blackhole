from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

  def findBottomLeftValue(self, root):
    # Initialize a queue with the root node
    queue = deque([root])

    # Initialize a variable to store the leftmost value
    leftmost_value = None

    # Perform level-order traversal (BFS)
    while queue:
      # Dequeue the current node
      node = queue.popleft()

      # Update the leftmost value with the value of the current node
      leftmost_value = node.val

      # Enqueue the right child first (if exists)
      if node.right:
        queue.append(node.right)
      # Enqueue the left child (if exists)
      if node.left:
        queue.append(node.left)

    # Return the leftmost value found after traversing all nodes
    return leftmost_value
