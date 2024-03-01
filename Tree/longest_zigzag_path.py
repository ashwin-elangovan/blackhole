

# Simple english no confusion :)

# Video: https://www.youtube.com/watch?v=t9GTh7uLZCA

# 2 recursions from root - One for left tree and anotehr for right subtree
# Direction 0 means left and 1 means right
# In left subtree, you have to go right to be zigzag. In that case, we'll add depth+1 and maintain the direction as 1 (for right). If you are going to left in the left subtree, then thats not zigzag and, the depth becomes 1 since the start of the zigzag path becomes the left child node from root.
# In right subtree, you have to go left to be zigzag. In that case, we'll add depth+1 and maintain the direction as 0 (for left). If you are going to right in the right subtree, then thats not zigzag and, the depth becomes 1 since the start of the zigzag path becomes the right child node from root.

class Solution:
    def longestZigZag(self, root):
        # Check if the root is None, if so, return None
        if not root:
            return None

        # Initialize a variable to keep track of the maximum length
        self.maxLen = 0

        # Define a depth-first search (DFS) function
        def dfs(root, depth, direction):
            # If the current node is None, return
            if not root:
                return
            
            # Update the maximum length if the current depth is greater
            self.maxLen = max(self.maxLen, depth)

            # Check the direction (0 for left, 1 for right)
            if direction == 0:
                # If the direction is left, explore the left subtree first (depth+1, direction 0)
                dfs(root.left, depth+1, 0)
                # Then explore the right subtree (depth+1, direction 1)
                dfs(root.right, depth+1, 1)
            else:
                # If the direction is right, explore the left subtree first (depth+1, direction 0)
                dfs(root.left, depth+1, 0)
                # Then explore the right subtree (depth+1, direction 1)
                dfs(root.right, depth+1, 1)

        # Start the DFS from both the left and right subtrees
        # Direction 0 means starting from the left, and 1 means starting from the right
        dfs(root.left, 1, 0)
        dfs(root.right, 1, 1)

        # Return the maximum length found during the traversal
        return self.maxLen
