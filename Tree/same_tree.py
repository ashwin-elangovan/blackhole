# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Base case: If both trees are empty, they are the same
    if p is None and q is None:
      return True

    # If one tree is empty but the other is not, or if the values of the current nodes are different, return False
    if p is None or q is None or p.val != q.val:
      return False

    # Recursively check if the left and right subtrees are the same
    return self.isSameTree(p.left, q.left) and self.isSameTree(
      p.right, q.right)
