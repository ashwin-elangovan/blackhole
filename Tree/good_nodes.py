# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Example 1:

# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.

# Logic: DFS through every path, and keep tracking of biggest value(curMax) in the path. If current node is >= the biggest value in the path, we add the answer by one.

# Solution: https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/2512547/c-python-c-97-dfs-detailed-graph-explantion-beginner-friendly-easy-to-understand/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0  # Initialize a count variable to keep track of good nodes
        
        if (root is None):
            return 0  # If the tree is empty, return 0 as there are no good nodes
        
        def dfs(root, currMax):
            nonlocal count  # Use nonlocal to access the count variable from the outer function
            
            if not root:
                return 0  # If the current node is None, return 0
            
            if (root.val >= currMax):
                count += 1  # If the current node's value is greater than or equal to the current maximum, increment the count
                currMax = root.val  # Update the current maximum
            
            dfs(root.left, currMax)  # Recursively call dfs on the left subtree
            dfs(root.right, currMax)  # Recursively call dfs on the right subtree

        dfs(root, root.val)  # Start the depth-first search (dfs) from the root node with the initial current maximum as root's value

        return count  # Return the count of good nodes in the binary tree
