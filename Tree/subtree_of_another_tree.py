# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Naive approach

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check if there's no more in the main tree (root)
        # to compare with the subRoot. If there's nothing left,
        # return False, as we couldn't find a matching subtree.
        if not root:
            return False
        
        # Check if the current subtree (root) matches the subRoot.
        # If they match, return True.
        if self.isMatch(root, subRoot):
            return True

        # If the current subtree doesn't match the subRoot, recursively
        # check in the left and right subtrees of the main tree (root).
        # Return True if either subtree has a matching subRoot.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatch(self, root, subRoot):
        # Check if both the current nodes in the main tree (root)
        # and the subRoot are None. If they are, it means we have
        # reached the end of both trees, and they match.
        if root is None and subRoot is None:
            return True

        # Check if either the current node in the main tree (root)
        # or the subRoot is None, but not both. In this case, the
        # trees don't match.
        if root is None or subRoot is None:
            return False

        # Check if the values of the current nodes in both trees match.
        # If they match, recursively check in the left and right subtrees.
        return (root.val == subRoot.val) and self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)

# Hashing approach

# Import the sha256 hash function from the hashlib library
from hashlib import sha256

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Define a hash function that takes a string x, updates it using SHA-256,
        # and returns the hexadecimal digest of the hash.
        def _hash(x):
            S = sha256()
            S.update(bytes(x, encoding='utf-8'))
            return S.hexdigest()
        
        # Define a function called 'merkle' that computes a Merkle tree hash for a given node.
        # The Merkle tree hash is a hash of the entire subtree rooted at the current node.
        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            # Compute the Merkle tree hash for the current node by concatenating the left subtree hash,
            # the current node's value, and the right subtree hash, and then hashing the result.
            node.merkle = _hash(m_left + str(node.val) + m_right)
            return node.merkle

        # Compute the Merkle tree hash for both the main tree (root) and the subRoot tree.
        merkle(root)
        merkle(subRoot)

        # Define a depth-first search function called 'dfs' that checks if there's a subtree in
        # the main tree (root) that matches the Merkle tree hash of the subRoot tree.
        def dfs(node):
            if not node:
                return False
            return (node.merkle == subRoot.merkle or 
                    dfs(node.left) or dfs(node.right))

        # Return the result of calling the 'dfs' function starting from the root of the main tree.
        return dfs(root)



        