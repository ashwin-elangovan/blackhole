# Python program to detect loop in the linked list
  
# Node class

# Floyd’s Cycle-Finding Algorithm:
#Follow the steps below to solve the problem:

#Traverse linked list using two pointers.
#Move one pointer(slow_p) by one and another pointer(fast_p) by two.
#If these pointers meet at the same node then there is a loop. If pointers do not meet then the linked list doesn’t have a loop.
  
  
class Node:
  
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    # Difference 
    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return 1
        return 0
  
  
# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
  
# Create a loop for testing
llist.head.next.next.next.next = llist.head
if(llist.detectLoop()):
    print("Loop Found")
else:
    print("No Loop")
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)




##########################################


# Python 3 program to find the number
# of nodes in loop in a linked list
# if loop is present
 
# Python Code to detect a loop and
# find the length of the loop
# Node defining class
 
 
# class Node:
 
#     # Function to make a node
#     def __init__(self, val):
#         self.val = val
#         self.next = None
 
# Linked List defining and loop
# length finding class
 
 
# class LinkedList:
 
#     # Function to initialize the
#     # head of the linked list
#     def __init__(self):
#         self.head = None
 
#     # Function to insert a new
#     # node at the end
#     def AddNode(self, val):
#         if self.head is None:
#             self.head = Node(val)
#         else:
#             curr = self.head
#             while(curr.next):
#                 curr = curr.next
#             curr.next = Node(val)
 
#     # Function to create a loop in the
#     # Linked List. This function creates
#     # a loop by connecting the last node
#     # to n^th node of the linked list,
#     # (counting first node as 1)
#     def CreateLoop(self, n):
 
#         # LoopNode is the connecting node to
#         # the last node of linked list
#         LoopNode = self.head
#         for _ in range(1, n):
#             LoopNode = LoopNode.next
 
#         # end is the last node of the Linked List
#         end = self.head
#         while(end.next):
#             end = end.next
 
#         # Creating the loop
#         end.next = LoopNode
 
#     # Function to detect the loop and return
#     # the length of the loop if the returned
#     # value is zero, that means that either
#     # the linked list is empty or the linked
#     # list doesn't have any loop
#     def detectLoop(self):
 
#         # if linked list is empty then there
#         # is no loop, so return 0
#         if self.head is None:
#             return 0
 
#         # Using Floyd’s Cycle-Finding
#         # Algorithm/ Slow-Fast Pointer Method
#         slow = self.head
#         fast = self.head
#         flag = 0  # to show that both slow and fast
#         # are at start of the Linked List
#         while(slow and slow.next and fast and
#               fast.next and fast.next.next):
#             if slow == fast and flag != 0:
 
#                 # Means loop is confirmed in the
#                 # Linked List. Now slow and fast
#                 # are both at the same node which
#                 # is part of the loop
#                 count = 1
#                 slow = slow.next
#                 while(slow != fast):
#                     slow = slow.next
#                     count += 1
#                 return count
 
#             slow = slow.next
#             fast = fast.next.next
#             flag = 1
#         return 0  # No loop
 
 
# # Setting up the code
# # Making a Linked List and adding the nodes
# myLL = LinkedList()
# myLL.AddNode(1)
# myLL.AddNode(2)
# myLL.AddNode(3)
# myLL.AddNode(4)
# myLL.AddNode(5)
 
# # Creating a loop in the linked List
# # Loop is created by connecting the
# # last node of linked list to n^th node
# # 1<= n <= len(LinkedList)
# myLL.CreateLoop(2)
 
# # Checking for Loop in the Linked List
# # and printing the length of the loop
# loopLength = myLL.detectLoop()
# if myLL.head is None:
#     print("Linked list is empty")
# else:
#     print(str(loopLength))
 
# This code is contributed by _Ashutosh