# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # Check if root is one of the nodes p or q
        if root in (p, q):
            return root

        # Traverse left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return a node, then root is the LCA
        if left and right:
            return root

        # If only one subtree returns a node, return that node (potential LCA)
        return left if left else right

# Example usage:
if __name__ == "__main__":
    # Create tree nodes
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Create a Solution instance
    solution = Solution()

    # Find the lowest common ancestor for nodes with values 5 and 1
    p = root.left
    q = root.right
    lca = solution.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.val)  # Output: 3
