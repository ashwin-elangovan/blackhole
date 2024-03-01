# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# High level walk through
# In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.

# This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
  
# Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.

# We just need to add the frequency of the oldPathSum to the result. Why?

# Imagine we have a binary tree and we are looking for paths with a specific sum, let's say the target sum is 8. As we traverse the tree, we keep track of the current path sum (the sum of values along the path from the root to the current node).

# Now, let's say at some point in our traversal, we are at a node where the current path sum is, say, 12. We have already seen this sum earlier in our traversal, let's say at a different node. This means that there must be a subpath between these two nodes that has a sum equal to our target sum of 8.

# So, if we know how many times we have seen the sum of 12 before, we can count how many different paths exist from that previous occurrence of 12 to the current node that have a sum of 8. These are all valid paths that satisfy the target sum.


# During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.

# Note: Since after DFS we'll go back to the parent node and go to a different route (left/right children), to avoid recounting, we are clearing it by 1. currPathSum will have the sum of the current path. Path's should be stright. Either left or right.

# Why? when move to a different branch, the currPathSum is no longer available, hence remove one.

# Someone mentioned that it is similar to backtracking; I agree with this. The variable "currPathSum" can be thought of as a "sum from root to the current node". The cache's job is to store all possible sum from root to the current node only.

# So say that we have a very simple case with target 5

#       10
#     /    \ 
#   5        2
#           / 
#         3
# When you are at root, your cache will be {10:1}
# When you are at left child, your cache will be {10: 1, 15: 1}.
# When you are at right child (2), your cache will be {10: 1, 15:0, 12:1}. This makes sense, as we see that there is no sum from root to node (2) that can add up to 15, all possible sum from root to (2) are stored in cache.
# When you are at right child (3), your cache will be {10:1, 15:1, 12:1}.

# By doing this, we make sure that we don't double count total sum "15" when we are in the right side of the tree.

# Solution: https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Initialize a variable to store the result
        self.result = 0

        # Initialize a dictionary to cache (remember) intermediate sums
        self.cache = {}

        # Start the depth-first search (DFS) from the root node
        self.dfs(root, targetSum, 0)

        # Return the final result
        return self.result

    def dfs(self, root, target, curr_sum):
        # Base case: If we reach a null (empty) node, return
        if root is None:
            return None
        
        # Calculate the current sum by adding the value of the current node
        curr_sum += root.val

        if curr_sum == target:
          self.result += 1

        # Check if there is a previous sum that, when subtracted from the current sum, equals the target
        # This means we have found a valid path that satisfies the target sum
        if (curr_sum - target) in self.cache:
            self.result += self.cache[curr_sum - target]

        # Update the cache with the current sum
        if curr_sum in self.cache:
            self.cache[curr_sum] += 1
        else:
            self.cache[curr_sum] = 1

        # Continue the DFS by exploring the left and right subtrees
        self.dfs(root.left, target, curr_sum)
        self.dfs(root.right, target, curr_sum)

        # After exploring both subtrees, subtract 1 from the current sum in the cache
        # This step is crucial to avoid counting the current sum in future paths
        self.cache[curr_sum] -= 1
