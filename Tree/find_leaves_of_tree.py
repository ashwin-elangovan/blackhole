"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict


class Solution:

  def __init__(self):
    # Initialize a defaultdict to store nodes based on their height
    self.final_val = defaultdict(lambda: [])

  def dfs(self, root):
    """
        Depth-first search (DFS) function to traverse the binary tree and collect leaves.

        Args:
        - root: The root node of the binary tree.

        Returns:
        - The height of the current node in the binary tree.
        """
    if not root:
      return -1
    # Recursively calculate the height of the current node
    curr_height = 1 + max(self.dfs(root.left), self.dfs(root.right))
    # Append the current node's value to the list corresponding to its height
    self.final_val[curr_height].append(root.val)
    return curr_height

  def findLeaves(self, root):
    """
        Finds and removes all leaves from the binary tree.

        Args:
        - root: The root node of the binary tree.

        Returns:
        - A list containing lists of values of leaves at each level of the binary tree.
        """
    if not root:
      return []
    # Perform DFS traversal to collect leaves and their heights
    self.dfs(root)
    # Return the values of leaves grouped by their heights
    return list(self.final_val.values())
