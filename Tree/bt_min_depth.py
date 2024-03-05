# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if root is None, return 0
        if not root:
            return 0

        # Initialize a variable to store the minimum depth
        self.min_depth = float('inf')

        # Helper function to perform depth-first search
        def dfs(root, cur_depth):
            # Base case: if root is None, return
            if not root:
                return

            # If the current node is a leaf node, update the minimum depth
            if not root.left and not root.right:
                self.min_depth = min(self.min_depth, cur_depth + 1)

            # Recursively traverse the left and right subtrees
            dfs(root.left, cur_depth + 1)
            dfs(root.right, cur_depth + 1)

        # Start the depth-first search from the root with initial depth 0
        dfs(root, 0)

        # Return the minimum depth of the tree
        return self.min_depth

if __name__ == "__main__":
  # Create binary tree: [3,9,20,null,null,15,7]
  root = TreeNode(3)
  root.left = TreeNode(9)
  root.right = TreeNode(20)
  root.right.left = TreeNode(15)
  root.right.right = TreeNode(7)

  # Create an instance of the Solution class
  solution = Solution()

  # Call minDepth function and print the result
  print(solution.minDepth(root))  # Output: 2
