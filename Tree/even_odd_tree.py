from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    # Check if the root is None
    if not root:
      # If root is None, return False (not an even-odd tree)
      return False

    # Initialize a queue with the root node
    q = deque([root])

    # Initialize a variable to track the level (even or odd)
    is_even = True

    # Loop until the queue is empty
    while q:
      # Initialize a variable to track the previous node
      prev = None

      # Process all nodes at the current level
      for _ in range(len(q)):
        # Dequeue the current node
        curr = q.popleft()

        # Check if the current node's value violates the even-odd property
        if is_even:
          # For even level, the node's value should be odd
          if curr.val % 2 == 0:
            return False
          # Check if the current node's value is greater than or equal to the previous node's value
          if prev and prev.val >= curr.val:
            return False
        else:
          # For odd level, the node's value should be even
          if curr.val % 2 != 0:
            return False
          # Check if the current node's value is less than or equal to the previous node's value
          if prev and prev.val <= curr.val:
            return False

        # Enqueue the left child if exists
        if curr.left:
          q.append(curr.left)
        # Enqueue the right child if exists
        if curr.right:
          q.append(curr.right)

        # Update the previous node
        prev = curr

      # Toggle the level (even to odd or odd to even)
      is_even = not is_even

    # If the loop completes without returning False, it means the tree satisfies the even-odd property
    return True
