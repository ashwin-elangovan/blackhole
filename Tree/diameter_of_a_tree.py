# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # Initialize a variable to store the maximum diameter
    ans = 0

    # Define a recursive function to calculate the height of each subtree
    def dfs(root):
      nonlocal ans  # Use the nonlocal keyword to modify the value of 'ans' inside the nested function
      if not root:
        return 0
      # Recursively calculate the height of the left and right subtrees
      sublheight = dfs(root.left)
      subrheight = dfs(root.right)
      # Update the maximum diameter if the sum of heights of the left and right subtrees is greater than the current maximum diameter
      ans = max(ans, sublheight + subrheight)
      # Return the height of the current subtree (maximum height of the left and right subtrees plus 1)
      return max(sublheight, subrheight) + 1

    # Call the dfs function to calculate the height of each subtree and update the maximum diameter
    dfs(root)
    # Return the maximum diameter of the binary tree
    return ans
