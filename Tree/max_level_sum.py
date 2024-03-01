# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2


# Importing the necessary data structures
from collections import deque

# Definition for a binary tree node.
# Each node has a value, a left child, and a right child.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        # Initialize a deque (double-ended queue) for level-order traversal
        q = deque()
        # Add the root node to the queue to start traversal
        q.append(root)
        # Initialize variables to keep track of the maximum sum, current level, and the answer
        max_sum = float('-inf')  # Start with negative infinity as the initial maximum sum
        level = 0  # Start at level 0 (the root level)
        ans = 0  # Initialize the answer (level with the maximum sum)

        # Start the level-order traversal
        while q:
            n = len(q)  # Get the number of nodes at the current level
            curr_sum = 0  # Initialize the sum of values at the current level

            level = level + 1  # Increment the current level for the next iteration

            # Iterate through all nodes at the current level
            for idx in range(1, n+1):
                node = q.popleft()  # Dequeue the first node in the queue

                curr_sum += node.val  # Add the value of the current node to the current sum

                # Enqueue the left child if it exists
                if(node.left):
                    q.append(node.left)

                # Enqueue the right child if it exists
                if node.right:
                    q.append(node.right)
            
            # Check if the current sum is greater than the maximum sum seen so far
            if curr_sum > max_sum:
                max_sum = curr_sum  # Update the maximum sum
                ans = level  # Update the answer to the current level
                
        # Return the level with the maximum sum
        return ans
