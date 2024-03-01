# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if the root is None (base case)
        if not root:
            return None

        # Check if both p and q are smaller than the current root value
        if p.val < root.val > q.val:
            # Recursively search in the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Check if both p and q are greater than the current root value
        elif p.val > root.val < q.val:
            # Recursively search in the right subtree
            return self.lowestCommonAncestor(root.right, p, q)

        # If neither of the above conditions is met, it means we have found the LCA
        return root

