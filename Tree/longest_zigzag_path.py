

# Simple english no confusion :)

# Video: https://www.youtube.com/watch?v=t9GTh7uLZCA

# 2 recursions from root - One for left tree and anotehr for right subtree
# Direction 0 means left and 1 means right
# In left subtree, you have to go right to be zigzag. In that case, we'll add depth+1 and maintain the direction as 1 (for right). If you are going to left in the left subtree, then thats not zigzag and, the depth becomes 1 since the start of the zigzag path becomes the left child node from root.
# In right subtree, you have to go left to be zigzag. In that case, we'll add depth+1 and maintain the direction as 0 (for left). If you are going to right in the right subtree, then thats not zigzag and, the depth becomes 1 since the start of the zigzag path becomes the right child node from root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Check if the root is None (empty tree)
        if not root:
            return 0

        max_len = 0  # Initialize variable to store the maximum length of ZigZag path encountered so far

        def dfs(root, is_left, curr_len):
            if not root:
                return

            nonlocal max_len  # Declare max_len as nonlocal to modify its value within the nested function

            # Update max_len with the maximum of current length and max_len
            max_len = max(max_len, curr_len)

            # Recursive calls for left and right subtrees based on the direction
            if is_left:
                dfs(root.left, False, curr_len + 1)  # Explore left child with direction set to False (left)
                dfs(root.right, True, 1)  # Explore right child with direction set to True (right)
            else:
                dfs(root.left, False, 1)  # Explore left child with direction set to False (left)
                dfs(root.right, True, curr_len + 1)  # Explore right child with direction set to True (right)


        # Perform depth-first search (DFS) with left and right directions from the root node
        dfs(root, True, 0)  # Explore left direction initially
        dfs(root, False, 0)  # Explore right direction initially

        return max_len

# Example input
# Input: [1, null, 2, 3, 4, null, null, null, 5, 6]
# Output: 3 (The longest ZigZag path is from node 2 to node 3 to node 4)

