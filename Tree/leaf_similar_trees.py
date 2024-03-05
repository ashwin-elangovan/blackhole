# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 
# Example 1:

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# Example 2:

# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Initialize lists to store leaf values of both trees
        leaves_1 = []
        leaves_2 = []

        # Helper function to perform depth-first search and collect leaf values
        def dfs(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)  # Add leaf value to the list

            # Recursively traverse left and right subtrees
            dfs(root.left, leaves)
            dfs(root.right, leaves)

        # Populate lists with leaf values of both trees using DFS
        dfs(root1, leaves_1)
        dfs(root2, leaves_2)

        # Check if the lists of leaf values are equal
        return leaves_1 == leaves_2


