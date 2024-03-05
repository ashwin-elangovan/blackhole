# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Intuition
# The intuition behind the solution is to recursively check if two binary trees are identical. If both trees are empty (null), they are considered identical. If only one tree is empty or the values of the current nodes are different, the trees are not identical. Otherwise, we recursively check if the left and right subtrees of both trees are identical.

# Approach
# Check the base case: if both trees are null, return true.
# Check if only one tree is null or the values of the current nodes are different, return false.
# Recursively check if the left subtrees of both trees are identical.
# Recursively check if the right subtrees of both trees are identical.
# Return the logical AND of the results from steps 3 and 4.
# Complexity

# Time complexity:
# The time complexity of the solution is O(min(N,M))O(min(N, M))O(min(N,M)), where N and M are the number of nodes in the two trees, respectively. This is because we need to visit each node once in order to compare their values. In the worst case, where both trees have the same number of nodes, the time complexity would be O(N).

# Space complexity:
# The space complexity of the solution isO(min(H1,H2))O(min(H1, H2))O(min(H1,H2)), where H1 and H2 are the heights of the two trees, respectively. This is because the space used by the recursive stack is determined by the height of the smaller tree. In the worst case, where one tree is significantly larger than the other, the space complexity would be closer to O(N) or O(M), depending on which tree is larger.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, they are the same.
        if p is None and q is None:
            return True
        
        # If one tree is empty while the other is not, they are not the same.
        if p is None or q is None:
            return False

        # If the current nodes have the same value and their left and right subtrees are the same,
        # then the trees are the same.
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
