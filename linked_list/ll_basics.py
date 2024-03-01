# Node class
class Node:

    # A constructor is called here
    def __init__(self, data):
        self.data = data  # Automatically assign data
        self.next = None  # Initialize next pointer as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Usual linkedlist insert used in most of the cases.
    def insertAtHead(self, new_data):
        # 1: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 2. Make next of new Node as head
        new_node.next = self.head
        # 3. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_data, new_data):
        # 1. check if the Linked List is empty or not
        if self.head is None:
            return

        # 2. Create new node & Put in the data
        new_node = Node(new_data)

        # 3. If prev_data is at the first position
        # if (prev_data == self.head.data):
        #     new_node.next = self.head.next
        #     self.head.next = new_node
        #     return

        # 4. check if the given prev_data exists
        head = self.head
        while (head.data != prev_data):
            head = head.next
            # Goes till last element
            if head == None:
                return
        new_node.next = head.next
        head.next = new_node

    def insertattail(self, new_data):

        # 1. Create a new node
        new_node = Node(new_data)

        # 2. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # 3. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 4. Change the next of last node
        last.next = new_node

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # Recursive function to print 
    # linked list in reverse order
    # here temp refers to llist head
    def printrev(self, temp):
        if temp:
            self.printrev(temp.next)
            print(temp.data, end = ' ')
        else:
            return

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):
        # Initialize current to head
        current = self.head
        # loop till current not equal to None
        while current:
            if current.data == x:
                return True  # data found
 
            current = current.next
 
        return False  # Data Not found

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count
        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count

    # Function to reverse the linked list
    def reverse(self):
        # Initially for the head, prev = None, current = self value and next = head.next
        prev = None
        current = self.head
        while(current):
            next = current.next
            current.next = prev
            # Shift one place. Make current as prev and next as current. 
            prev = current
            current = next
        # Finally set the last value as head. Since current becomes None and prev becomes the last node
        self.head = prev

    # Method to reverse the list using recursion
    def reverse(self, head):
 
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = self.reverse(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None
 
        # Fix the header pointer
        return rest

    # Function to delete an entire linkedlist
    def deleteList(self):
        # initialize the current node
        current = self.head
        while current:
            next_to_current = current.next  # move next node
 
            # delete the current node
            del current.data
 
            # set current equals prev node
            current = next_to_current

        # In python garbage collection happens therefore, only
        # self.head = None
        # would also delete the link list

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node
  
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
  
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        assert(false)
        return 0

    # Function to get the nth node from
    # the last of a linked list
    def printNthFromLast(self, n):
        temp = self.head  # Used temp variable
  
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
  
        # Print count
        if n > length:  # If entered location is greater
                       # than length of linked list
            print('Location is greater than the' + ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def deleteNode(self, key):

        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def deleteNodeAtGivenPosition(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next
            # current = None # Optional statement

    def printMiddle(self, head):
        if head != None:
            # find length
            len = self.getCount()
            temp = head
 
            # traverse till we reached half of length
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
 
            # temp will be storing middle element
            print('The middle element is [%d]' % temp.data)

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):

            # If we already have
            # this node in hashmap it
            # means there is a cycle
            # (Because we are encountering
            # the node second time).
            if (temp in s):
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
  
            temp = temp.next
        return False

    

# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.insertAtHead(1)
    llist.insertAtHead(2)
    print("After insertion at head:", end=" ")
    llist.printList()
    print()

    llist.insertattail(4)
    llist.insertattail(5)
    print("After insertion at tail:", end=" ")
    llist.printList()
    print()

    llist.insertAfter(1, 2)
    llist.insertAfter(5, 6)
    print("After insertion at a given position:", end=" ")
    llist.printList()

    llist.printrev(llist.head)

    llist.search(21)

    llist.getCount()

    llist.reverse()