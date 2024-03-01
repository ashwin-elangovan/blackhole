# A utility class that represents
# an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# Inserting a new node with the given key
# Base case: root is None -> create and return
# If value == key, return root
# Else check key wrt value and recurse
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root,key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)


def minValueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 
# Given a binary search tree and a key, this function
# delete the key and returns the new root

# Follow the below steps to solve the problem:

# If the root is NULL, then return root (Base case)
# If the key is less than the root’s value, then set root->left = deleteNode(root->left, key)
# If the key is greater than the root’s value, then set root->right = deleteNode(root->right, key)
# Else check
# If the root is a leaf node then return null
# else if it has only the left child, then return the left child
# else if it has only the right child, then return the right child
# else set the value of root as of its inorder successor and recur to delete the node with the value of the inorder successor
# Return
 
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root
 
# Set The middle element of the array as root.
# Recursively do the same for the left half and right half.
# Get the middle of the left half and make it the left child of the root created in step 1.
# Get the middle of the right half and make it the right child of the root created in step 1.
# Print the preorder of the tree.
# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
     
    if not arr:
        return None
 
    # find middle index
    mid = (len(arr)) // 2
     
    # make the middle element the root
    root = Node(arr[mid])
     
    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])
     
    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

# Convert a normal BST to Balanced BST
# Traverse given BST in inorder and store result in an array. This step takes O(n) time. 
# Note that this array would be sorted as inorder traversal of BST always produces sorted sequence.
# Build a balanced BST from the above created sorted array using the recursive approach discussed here. 
# This step also takes O(n) time as we traverse every element exactly once and processing an element takes O(1) time.
 
# A utility function to print the preorder
# traversal of the BST
def preOrder(node):
    if not node:
        return
     
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

# Time Complexity: O(N)
# Auxiliary Space: O(H) ~= O(log(N)), for recursive stack space where H is the height of the tree.
# Convert a normal BST to Balanced BST
# This function traverse the skewed binary tree and
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root,nodes):
    # Base case
    if not root:
        return
     
    # Store nodes in Inorder (which is sorted
    # order for BST)
    storeBSTNodes(root.left,nodes)
    nodes.append(root)
    storeBSTNodes(root.right,nodes)
 
# Recursive function to construct binary tree
def buildTreeUtil(nodes,start,end):
     
    # base case
    if start>end:
        return None
 
    # Get the middle element and make it root
    mid=(start+end)//2
    node=nodes[mid]
 
    # Using index in Inorder traversal, construct
    # left and right subtress
    node.left=buildTreeUtil(nodes,start,mid-1)
    node.right=buildTreeUtil(nodes,mid+1,end)
    return node
 
# This functions converts an unbalanced BST to
# a balanced BST
def buildTree(root):
     
    # Store nodes of given BST in sorted order
    nodes=[]
    storeBSTNodes(root,nodes)
 
    # Constructs BST from nodes[]
    n=len(nodes)
    return buildTreeUtil(nodes,0,n-1)


######################
 
# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end =" ")
        inorder(root.right)

# Function to do preorder traversal of tree
def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)

# Function to find LCA of n1 and n2.
# The function assumes that both
#   n1 and n2 are present in BST
def lca(root, n1, n2):
    while root:
        # If both n1 and n2 are smaller than root,
        # then LCA lies in left
        if root.data > n1 and root.data > n2:
            root = root.left
 
        # If both n1 and n2 are greater than root,
        # then LCA lies in right
        elif root.data < n1 and root.data < n2:
            root = root.right
 
        else:
            break
 
    return root

# Follow the below steps to solve the problem:
# Do In-Order Traversal of the given tree and store the result in a temp array. 
# This method assumes that there are no duplicate values in the tree
# Check if the temp array is sorted in ascending order, if it is, then the tree is BST.
# Note: We can avoid the use of an Auxiliary Array. While doing In-Order traversal, we can keep track of previously visited nodes. If the value of the currently visited node is less than the previous value, then the tree is not BST.

def isBST(root, floor=float('-inf'), ceil=float('inf')):
  if root is None:
    return True
  if not floor < root.data < ceil:
    return False
  return isBST(root.left, floor, root.data) and isBST(root.right, root.data, ceil)
    

# Following is a 3 step solution for converting Binary tree to Binary Search Tree.

# Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
# Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
# Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.
 
# Helper function to store the inorder traversal of a tree
def storeInorder(root, inorder):
     
    # Base Case
    if root is None:
        return
     
    # First store the left subtree
    storeInorder(root.left, inorder)
     
    # Copy the root's data
    inorder.append(root.data)
 
    # Finally store the right subtree
    storeInorder(root.right, inorder)
 
# A helper function to count nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0
 
    return countNodes(root.left) + countNodes(root.right) + 1
 
# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):
 
    # Base Case
    if root is None:
        return
     
    # First update the left subtree
    arrayToBST(arr, root.left)
 
    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)
 
    # Finally update the right subtree
    arrayToBST(arr, root.right)
 
# This function converts a given binary tree to BST
def binaryTreeToBST(root):
     
    # Base Case: Tree is empty
    if root is None:
        return
     
    # Count the number of nodes in Binary Tree so that
    # we know the size of temporary array to be created
    n = countNodes(root)
 
    # Create the temp array and store the inorder traversal
    # of tree
    arr = []
    storeInorder(root, arr)
     
    # Sort the array
    arr.sort()
 
    # copy array elements back to binary tree
    arrayToBST(arr, root)
 
# Print the inorder traversal of the tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data,end=" ")
    printInorder(root.right)

# Complexity Analysis:

# Time Complexity: O(nlogn). This is the complexity of the sorting algorithm which we are using after first in-order traversal, rest of the operations take place in linear time.
# Auxiliary Space: O(n). Use of data structure ‘array’ to store in-order traversal.

""" Given a non-empty binary search tree, 
return the minimum data value found in that
tree. Note that the entire tree does not need
to be searched. """
 
 
def minValue(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current.data

# Time Complexity: O(Height of the BST)
# Auxiliary Space: O(1)

# Function to find the node with maximum value
# i.e. rightmost leaf node
def maxValue(root):
    current = root
     
    #loop down to find the rightmost leaf
    while(current.right):
        current = current.right
    return current.data

# A function to find 2nd largest 
# element in a given tree. 
def secondLargestUtil(root, c):
      
    # Base cases, the second condition 
    # is important to avoid unnecessary
    # recursive calls 
    if root == None or c[0] >= 2: 
        return
  
    # Follow reverse inorder traversal so that 
    # the largest element is visited first 
    secondLargestUtil(root.right, c)
  
    # Increment count of visited nodes 
    c[0] += 1
  
    # If c becomes k now, then this is
    # the 2nd largest 
    if c[0] == 2:
        print("2nd largest element is", 
                              root.key) 
        return
  
    # Recur for left subtree 
    secondLargestUtil(root.left, c)
  
# Function to find 2nd largest element 
def secondLargest(root):
      
    # Initialize count of nodes 
    # visited as 0 
    c = [0] 
  
    # Note that c is passed by reference 
    secondLargestUtil(root, c)

#############################

# BST Node contain to extra fields : Lcount , Sum

# For each Node of BST
# lCount : store how many left child it has
# Sum     : store sum of all left child it has

# Find Kth smallest element
# [ temp_sum store sum of all element less than equal to K ]

# ksmallestElementSumRec(root, K, temp_sum)

#   IF root -> lCount == K + 1
#       temp_sum += root->data + root->sum;
#       break;
#   ELSE
#      IF k > root->lCount   // Goto right sub-tree
#         temp_sum += root->data + root-> sum;
#         ksmallestElementSumRec(root->right, K-root->lcount+1, temp_sum)
#      ELSE
#         // Goto left sun-tree
#         ksmallestElementSumRec( root->left, K, temp_sum)
 
# function return sum of all element smaller
# than and equal to Kth smallest element

# A utility function to insert a new Node with
# given key in BST and also maintain lcount ,Sum
def insert(root, key):
     
    # If the tree is empty, return a new Node
    if root == None:
        return createNode(key)
 
    # Otherwise, recur down the tree
    if root.data > key:
         
        # increment lCount of current Node
        root.lCount += 1
 
        # increment current Node sum by
        # adding key into it
        root.Sum += key
 
        root.left= insert(root.left , key)
    else if root.data < key:
        root.right= insert (root.right , key)
 
    # return the (unchanged) Node pointer
    return root

def ksmallestElementSumRec(root, k , temp_sum):
    if root == None:
        return
 
    # if we fount k smallest element
    # then break the function
    if (root.lCount + 1) == k:
        temp_sum[0] += root.data + root.Sum
        return
 
    else if k > root.lCount:
         
        # store sum of all element smaller
        # than current root ;
        temp_sum[0] += root.data + root.Sum
 
        # decremented k and call right sub-tree
        k = k -( root.lCount + 1)
        ksmallestElementSumRec(root.right,
                               k, temp_sum)
    else: # call left sub-tree
        ksmallestElementSumRec(root.left,
                               k, temp_sum)
 
# Wrapper over ksmallestElementSumRec()
def ksmallestElementSum(root, k):
    Sum = [0]
    ksmallestElementSumRec(root, k, Sum)
    return Sum[0]

###############################
# Not so efficient
INT_MAX = 2147483647

# function return sum of all element smaller
# than and equal to Kth smallest element
def ksmallestElementSumRec(root, k, count) :
 
    # Base cases
    if (root == None) :
        return 0
    if (count[0] > k[0]) :
        return 0
 
    # Compute sum of elements in left subtree
    res = ksmallestElementSumRec(root.left, k, count)
    if (count[0] >= k[0]) :
        return res
 
    # Add root's data
    res += root.data
 
    # Add current Node
    count[0] += 1
    if (count[0] >= k[0]) :
        return res
 
    # If count is less than k, return
    # right subtree Nodes
    return res + ksmallestElementSumRec(root.right,
                                        k, count)
 
# Wrapper over ksmallestElementSumRec()
def ksmallestElementSum(root, k):
    count = [0]
    return ksmallestElementSumRec(root, k, count)

# Time complexity: O(k)
# Auxiliary Space: O(h), where h is the height of the tree

###################################
 
# function to insert elements of the
# tree to map m
def storeInorder(root):
 
    if (root == None):
        return
    storeInorder(root.left)
    v.append(root.data)
    storeInorder(root.right)
 
# function to check if the two BSTs contain
# same set of elements
def checkBSTs(root1, root2):
 
    # Base cases
    if (root1 == None and root2 == None) :
        return True
    if ((root1 == None and root2 != None) or \
        (root1 != None and root2 == None)):
        return False
         
    # Create two hash sets and store
    # elements both BSTs in them.
    v1 = []
    v2 = []
    v = v1
    storeInorder(root1)
    v1 = v
    v = v2
    storeInorder(root2)
    v2 = v
     
    # Return True if both hash sets
    # contain same elements.
    return (v1 == v2)


# Driver program to test the above functions
if __name__ == '__main__':
 
    # Let us create the following BST
    # 50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80
 
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
 
    # Print inoder traversal of the BST
    inorder(r)

    root = deleteNode(root, 20)

    root = buildTree(root)

    # Function calls
    n1 = 10
    n2 = 14
    t = lca(root, n1, n2)

    # Function call
    if (isBST(root) == None):
        print("Is BST")
    else:
        print("Not a BST")

    secondLargest(root)

    # check if two BSTs have same set of elements
    if (checkBSTs(root1, root2)):
        print("YES")
    else:
        print("NO")

    k = [3]
    print(ksmallestElementSum(root, k))
