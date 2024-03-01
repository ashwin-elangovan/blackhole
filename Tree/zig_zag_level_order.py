# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the root is empty, return an empty list.

        queue = deque([root])  # Create a deque and initialize it with the root node.
        res = []  # Initialize an empty list to store the result.

        direction = 1  # Direction variable to control zigzag order (1 for left to right, -1 for right to left).

        while queue:
            level = []  # Initialize an empty list to store values at the current level.
            for element in range(len(queue)):
                node = queue.popleft()  # Remove the node at the front of the queue.
                level.append(node.val)  # Add its value to the current level list.

                # Add left and right children to the queue if they exist.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level[::direction])  # Append the current level list to the result list, with the direction applied.
            direction *= -1  # Reverse the direction for the next level (zigzag).

        return res  # Return the zigzag level order traversal as a list of lists.
