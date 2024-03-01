# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Base case...
        # If the subtree is empty i.e. root is NULL, return depth as 0...
        if root is None:  return 0
        # Initialize the depth of two subtrees...
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        # If the both subtrees are empty...
        if root.left is None and root.right is None:
            return 1
        # If the left subtree is empty, return the depth of right subtree after adding 1 to it...
        if root.left is None:
            return 1 + rightDepth
        # If the right subtree is empty, return the depth of left subtree after adding 1 to it...
        if root.right is None:
            return 1 + leftDepth
        # When the two child function return its depth...
        # Pick the minimum out of these two subtrees and return this value after adding 1 to it...
        return min(leftDepth, rightDepth) + 1;    # Adding 1 is the current node which is the parent of the two subtrees...