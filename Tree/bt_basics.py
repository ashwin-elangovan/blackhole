
from collections import deque, defaultdict

class newNode():
 
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
         

# Algorithm Inorder(tree)
# Traverse the left subtree, i.e., call Inorder(left->subtree)
# Visit the root.
# Traverse the right subtree, i.e., call Inorder(right->subtree)
# In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)

# Algorithm Preorder(tree)
# Visit the root.
# Traverse the left subtree, i.e., call Preorder(left->subtree)
# Traverse the right subtree, i.e., call Preorder(right->subtree)
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val)
        # Then recur on left child
        printPreorder(root.left)
        # Finally recur on right child
        printPreorder(root.right) 

# Algorithm Postorder(tree)

# Traverse the left subtree, i.e., call Postorder(left->subtree)
# Traverse the right subtree, i.e., call Postorder(right->subtree)
# Visit the root

# Postorder traversal is used to delete the tree. 
# We should use the postorder traversal because before deleting the parent node, we should delete its child nodes first.

# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # the recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val)

# Iterative Method to print the
# height of a binary tree
def printLevelOrder(root):
 
    # Base Case
    if root is None:
        return
 
    # Create an empty queue
    # for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
 
    while(len(queue) > 0):
 
        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end=" ")
        node = queue.pop(0)
 
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
 
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

 
def insert(root, key):
    # If key is not there, create a newNode
    if not root:
        return newNode(key)

    q = []
    q.append(root)

    # Do level order traversal until we find
    # an empty place.
    while (q):
        # Assign the root and pop
        temp = q[0]
        q.pop(0)

        # If left is not there, assign and break
        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            # Add it to q so the traversal goes to next level
            q.append(temp.left)

        # If right is not there, assign and break 
        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

def deepestNode(root):
    q = []
    q.append(root)
    while(q):
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    print(temp.key)

# Starting at the root, find the deepest and rightmost node in the binary tree and the node which we want to delete. 
# Replace the deepest rightmost node’s data with the node to be deleted. 
# Then delete the deepest rightmost node.
def deletion(root, key):
    if(not root):
        return None
    if(not root.left and not root.right):
        if(root.data == key):
            # Since this None is assigned to root in the main function, it doesn't matter.
            return None
        else:
            return root
 
    key_node = None # Deepest rightmost node [node to be deleted (key_node)]
    temp = None # Ultimately will hold deepest node data
    last_node_parent = None # parent of deepest node(last)
    
    q = []
    q.append(root)
    # Do level order traversal to find deepest
    # node(temp), node to be deleted (key_node)
    # and parent of deepest node(last)
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp # Node to be deleted
        if temp.left:
            key_node_parent = temp  # storing the parent node of the deepest node
            q.append(temp.left)
        if temp.right:
            key_node_parent = temp  # storing the parent node of the deepest node
            q.append(temp.right)

    # temp will contain the last element's value
    if key_node:
        key_node.data = temp.data  # replacing key_node_parent's data to deepest node's data
        if key_node_parent.right == temp:
            key_node_parent.right = None
        else:
            key_node_parent.left = None
    return root

# Deletes a tree and sets the root as NULL
# Level order traverses the tree and sets node to None.
def deleteTree(node):
    if node:
        deleteTree(node.left)
        deleteTree(node.right)
        node = None

# BFS level order traversal
# DFS = Preorder, Inorder, Postorder

# Level Order Binary Tree Traversal = BFS
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    queue = []
    queue.append(root)

    while(queue):
        print(queue[0].data, end = " ")
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Easy recursion construction:
# 1) Consider the case for just root and its children
# 2) Construct an end case

# Function to find height of tree using BFS
def height_by_bfs(root):
    # Base Case
    if root is None:
        return 0

    q = []
    q.append(root)
    height = 0
   
    # Loop while queue is not empty
    while q:
        # nodeCount (queue size) indicates number of nodes at current level
        nodeCount = len(q)

        # Dequeue all nodes of current level and Enqueue all nodes of next level
        while nodeCount > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1
        # Add one to height as we are going to next level
        height += 1
   
    return height

# Function to find height of tree using DFS recursion
def height(root):
    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight + 1
    else: # This handles the case for leaf node where lheight and rheight will be 0
        return rheight + 1

# Computes the number of nodes in tree. Size is kinda similar to height but in height we'll take only left or right and add one. Here we'll consider both the sides and add one.
def size(node):
    if node:
        return (size(node.left) + 1 + size(node.right))
    return 0

def findMax(root):
    if root is None:
        return float('-inf')

    # Return maximum of 3 values:
    # 1) Root's data
    # 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    return max(res, lres, rres)

def findMin(root):
    if root is None:
        return float('inf')
    # Return minimum of 3 values:
    # 1) Root's data
    # 2) Min in Left Subtree
    # 3) Min in right subtree
    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)
    return min(res, lres, rres)

# The left view contains all nodes that are the first nodes in their levels. 
# A simple solution is to do level order traversal and print the first node in every level.       
def printLeftView(root):
    if (not root):
        return

    q = []
    q.append(root)
 
    while q:
        # number of nodes at current level
        n = len(q)
 
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
 
            # Print the left most element at the level
            if (i == 1):
                print(temp.data, end=" ")

            # Add left node to queue
            if (temp.left != None):
                q.append(temp.left)
 
            # Add right node to queue
            if (temp.right != None):
                q.append(temp.right)

def rightView(root):

    if root is None:
        return

    q = deque()
    q.append(root)

    while q:

        # Get number of nodes for each level
        n = len(q)

        # Traverse all the nodes of the
        # current level

        while n > 0:
            n -= 1

            # Get the front node in the queue
            node = q.popleft()

            # Print the last node of each level
            if n == 0:
                print(node.data, end=" ")

            # If left child is not null push it
            # into the queue
            if node.left:
                q.append(node.left)

            # If right child is not null push
            # it into the queue
            if node.right:
                q.append(node.right)

# The lowest common ancestor is the lowest node in the tree that has both n1 and n2 as descendants, 
# where n1 and n2 are the nodes for which we wish to find the LCA. 
# Hence, the LCA of a binary tree with nodes n1 and n2 is the shared ancestor of n1 and n2 that is located farthest from the root. 

def find(root, k):
    # Base Case
    if root is None:
        return False

    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or
            find(root.right, k)):
        return True
 
    # Else return false
    return False

def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    # the presence by returning root (Note that if a key is
    # ancestor of other, then the ancestor key becomes LCA)
    if root.key == n1 or root.key == n2:
        return root
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

# This approach is based on the level order traversal. We’ll keep a record of the current max so far left, and right horizontal distances from the root.
# And if we found less distance (or greater in magnitude) than max left so far distance then update it and also push data on this node to a stack (stack is used because in level order traversal the left nodes will appear in reverse order)
# If we found a greater distance then max right so far distance then update it and also push data on this node to a vector.
# In this approach, no map is used.
import collections
# Topview
class Tree:
    def __init__(self):
        self.root = None
 
    def topView(self):
 
        # queue for holding nodes and their horizontal
        # distance from the root node
        q = []
 
        # pushing root node with distance 0
        q.append((self.root, 0))
 
        # hd is current node's horizontal distance from
        #  root node l is current left min horizontal
        #  distance (or max in magnitude) so far from the
        #  root node r is current right max horizontal
        # distance so far from the root node
 
        hd = 0
        l = 0
        r = 0
 
        # stack is for holding left node's data because
        # they will appear in reverse order that is why
        # using stack
        left = collections.deque([])
 
        # list is for holding right node's data
        right = collections.deque([])
 
        while len(q) > 0:
            node, hd = q[0]
 
            if hd < l:
                left.append(node.data)
                l = hd
 
            elif hd > r:
                right.append(node.data)
                r = hd
 
            if node.left != None:
                q.append((node.left, hd-1))
 
            if node.right != None:
                q.append((node.right, hd+1))

            q.pop(0)
 
        # printing the left node's data in reverse order
        for x in left:
            print(x, end=" ")
 
        # then printing the root node's data
        print(self.root.data, end=" ")
 
        # finally printing the right node's data
        for x in right:
            print(x, end=" ")

# Create a unordered_map where the key is the horizontal distance and the value is a int x, where x is the value of the node .
# Perform a level order traversal of the tree. 
# For every node at a horizontal distance of h we will store its value in unordered_map<int,int>  (eg <vertical_index , root->data> ). 
from collections import defaultdict, deque

def printBottomView(root):
    if root is None: return #if root is NULL
    hash = defaultdict(lambda : 0) # <vertical_index , root->data>
    leftmost = 0 # to store the leftmost index so that we move from left to right
    q = deque() # pair<Node*,vertical Index>  for level order traversal.
    q.append((root, 0)) # push the root and 0 vertial index
    while q:
        top = q.popleft() #  store q.front() in top variable
        temp, ind = top # store the Node in temp for left and right nodes and store the vertical index of current node
        print("Temp", temp)
        print("Ind", ind)
        hash[ind] = temp.data # store the latest vertical_index(key) -> root->data(value)
        leftmost = min(ind, leftmost) # have the leftmost vertical index
        if temp.left: q.append((temp.left, ind-1)) # check if any node of left then go in negative direction
        if temp.right: q.append((temp.right, ind+1)) #check if any node of left then go in positive direction
    #Traverse each value in hash from leftmost to positive side till key is available
    for i in range(leftmost, len(hash)):
          if hash[i]:
            print(hash[i], end=" ")

# def diameter

# Driver code
if __name__ == '__main__':

    # Binary tree construction
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)

    key = 11
    root = deletion(root, key)

    # It may cause problems if the user of deleteTree() doesn’t change root to NULL and tries to access the values using the root pointer.
    deleteTree(root)
    root = None

    # Do a find before doing findLCA
    res1 = find(root, 4)
    res2 = find(root, 10)
    if res1 and res2:
        lca = findLCA(root, 4, 10)


