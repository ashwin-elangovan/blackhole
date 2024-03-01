
# Python program to
# demonstrate stack implementation
# using list
 
stack = []
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

########

# Queue using Stacks

# Method 1 (By making enQueue operation costly): This method makes sure that oldest entered element is always at the top of stack 1, 
# so that deQueue operation just pops from stack1. To put the element at top of stack1, stack2 is used.
# enQueue(q, x): 

# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# Here time complexity will be O(n)

# deQueue(q): 
# If stack1 is empty then error
# Pop an item from stack1 and return it
# Here time complexity will be O(1)

# Python3 program to implement Queue using 
# two stacks with costly enQueue() 
  
class Queue: 
    def __init__(self):
        self.s1 = []
        self.s2 = []
  
    def enQueue(self, x):  
        # Move all elements from s1 to s2 
        while len(self.s1) != 0: 
            self.s2.append(self.s1[-1]) 
            self.s1.pop()
  
        # Push item into self.s1 
        self.s1.append(x) 
  
        # Push everything back to s1 
        while len(self.s2) != 0: 
            self.s1.append(self.s2[-1]) 
            self.s2.pop()
  
    # Dequeue an item from the queue 
    def deQueue(self):  
        # if first stack is empty 
        if len(self.s1) == 0: 
            print("Q is Empty")
      
        # Return top of self.s1 
        x = self.s1[-1] 
        self.s1.pop() 
        return x
  
# Driver code 
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1) 
    q.enQueue(2) 
    q.enQueue(3) 
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

# Method 2 (By making deQueue operation costly): In this method, in en-queue operation, the new element is entered at the top of stack1. In de-queue operation, if stack2 is empty then all the elements are moved to stack2 and finally top of stack2 is returned. 

# enQueue(q,  x)
#   1) Push x to stack1 (assuming size of stacks is unlimited).
# Here time complexity will be O(1)

# deQueue(q)
#   1) If both stacks are empty then error.
#   2) If stack2 is empty
#        While stack1 is not empty, push everything from stack1 to stack2.
#   3) Pop the element from stack2 and return it.
# Here time complexity will be O(n)

# Method 2 is definitely better than method 1. 

# Method 1 moves all the elements twice in enQueue operation, while method 2 (in deQueue operation) moves the elements once and moves elements only if stack2 empty. So, the amortized complexity of the dequeue operation becomes O(1)

# Implementation of method 2:


# Python3 program to implement Queue using 
# two stacks with costly deQueue()
  
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
  
    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.append(x)
  
    # DeQueue item from the queue
    def deQueue(self):
  
        # if both the stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
  
        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
  
        else:
            return self.s2.pop()
  
    # Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
  
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())

####################

# Python3 program to implement stack using a single queue
  
q = []
# append operation
def append(val):
    # get previous size of queue
    size = len(q)
    # Add current element
    q.append(val);
    # Pop (or Dequeue) all previous
    # elements and put them after current
    # element
    for i in range(size):
        # this will add front element into
        # rear of queue
        x = q.pop(0);
        q.append(x);
            
# Removes the top element
def pop():
    if (len(q) == 0):
        print("No elements");
        return -1;
    x = q.pop(0);
    return x;
 
# Returns top of stack
def top():
    if(len(q) == 0):
        return -1;
    return q[0]
 
# Returns true if Stack is empty else false
def isEmpty():
    return len(q)==0;
 
# Driver program to test above methods
if __name__=='__main__':
    s = []
    s.append(10);
    s.append(20);
    print("Top element :" + str(s[-1]));
    s.pop();
    s.append(30);
    s.pop();
    print("Top element :" + str(s[-1]));

##################

# In priority queue, we assign priority to the elements that are being pushed. A stack requires elements to be processed in Last in First Out manner.
# The idea is to associate a count that determines when it was pushed. This count works as a key for the priority queue.
# So the implementation of stack uses a priority queue of pairs, with the first element serving as the key.

import heapq
 
# User defined stack class
class Stack:
    # cnt is used to keep track of the number of
    # elements in the stack and also serves as key
    # for the priority queue.
    def __init__(self):
        self.cnt = 0
        self.pq = []
 
    def push(self, n):
        # push function increases cnt by 1 and
        # inserts this cnt with the original value.
        self.cnt += 1
        heapq.heappush(self.pq, (-self.cnt, n))
 
    def pop(self):
        # pops element and reduces count.
        if not self.pq:
            print("Nothing to pop!!!")
        self.cnt -= 1
        return heapq.heappop(self.pq)[1]
 
    def top(self):
        # returns the top element in the stack using
        # cnt as key to determine top(highest priority),
        # default comparator for pairs works fine in this case
        return self.pq[0][1]
 
    def isEmpty(self):
        # return true if stack is empty
        return not bool(self.pq)
 
# Driver code
s = Stack()
s.push(1)
s.push(2)
s.push(3)
while not s.isEmpty():
    print(s.top())
    s.pop()

########################

# Create a stack and push all the elements in it.
# Call reverse(), which will pop all the elements from the stack and pass the popped element to function insert_at_bottom()
# Whenever insert_at_bottom() is called it will insert the passed element at the bottom of the stack.
# Print the stack  

# Python3 program to check for
# balanced brackets.
 
# function to check if
# brackets are balanced
 
 
def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 
 ##################

# Python program to reverse a
# stack using recursion
 
# Below is a recursive function
# that inserts an element
# at the bottom of a stack.
 
 
def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
# Below is the function that
# reverses the given stack
# using insertAtBottom()
 
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
 
# Below is a complete running
# program for testing above
# functions.
 
# Function to create a stack.
# It initializes size of stack
# as 0
 
 
def createStack():
    stack = []
    return stack
 
# Function to check if
# the stack is empty
 
 
def isEmpty(stack):
    return len(stack) == 0
 
# Function to push an
# item to stack
 
 
def push(stack, item):
    stack.append(item)
 
# Function to pop an
# item from stack
 
 
def pop(stack):
 
    # If stack is empty
    # then error
    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
# Function to print the stack
 
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
# Driver Code
 
 
stack = createStack()
push(stack, str(4))
push(stack, str(3))
push(stack, str(2))
push(stack, str(1))
print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)

##################

# Create an empty stack.
# One by one push all characters of string to stack.
# One by one pop all characters from stack and put them back to string.
# Python program to reverse a string using stack
 
# Function to create an empty stack.
# It initializes size of stack as 0
 
 
def createStack():
    stack = []
    return stack
 
# Function to determine the size of the stack
 
 
def size(stack):
    return len(stack)
 
# Stack is empty if the size is 0
 
 
def isEmpty(stack):
    if size(stack) == 0:
        return true
 
# Function to add an item to stack .
# It increases size by 1
 
 
def push(stack, item):
    stack.append(item)
 
# Function to remove an item from stack.
# It decreases size by 1
 
 
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()
 
# A stack based function to reverse a string

def reverse(string):
    n = len(string)
 
    # Create a empty stack
    stack = createStack()
 
    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])
 
    # Making the string empty since all
    # characters are saved in stack
    string = ""
 
    # Pop all characters of string and
    # put them back to string
    for i in range(0, n, 1):
        string += pop(stack)
 
    return string
 
 
# Driver program to test above functions
string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)

############

# In this approach, I have used the data structure stack to implement this task.
# Here, two stacks are used. One stack stores the actual stock prices whereas, the other stack is a temporary stack.
# The stock span problem is solved using only the Push and Pop functions of the Stack.
# Just to take input values, I have taken array ‘price’ and to store output, used array ‘span’.

# The stock span problem is a financial problem where we have a series of N daily price quotes for a stock and we need to calculate the span of the stock’s price for all N days. The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than its price on the given day. 

# Examples:

# Input: N = 7, price[] = [100 80 60 70 60 75 85]
# Output: 1 1 1 2 1 4 6
# Explanation: Traversing the given input span for 100 will be 1, 80 is smaller than 100 so the span is 1, 60 is smaller than 80 so the span is 1, 70 is greater than 60 so the span is 2 and so on. Hence the output will be 1 1 1 2 1 4 6.

# Input: N = 6, price[] = [10 4 5 90 120 80]
# Output:1 1 2 4 5 1
# Explanation: Traversing the given input span for 10 will be 1, 4 is smaller than 10 so the span will be 1, 5 is greater than 4 so the span will be 2 and so on. Hence, the output will be 1 1 2 4 5 1.

# Python3 program for a linear time
# solution for stock span problem
# using stack

def calculateSpan(a, n):
    s = []
    ans = []
    for i in range(0, n):
 
        while(s != [] and a[s[-1]] <= a[i]):
            s.pop()
 
        if(s == []):
            ans.append(i+1)
 
        else:
            top = s[-1]
            ans.append(i - top)
 
        s.append(i)
 
    return ans

# A utility function to print elements of array

def printArray(arr, n):
 
    for i in range(n):
        print(arr[i], end=' ')
    print()

# Driver code
price = [10, 4, 5, 90, 120, 80]
n = len(price)
ans = calculateSpan(price, n)
 
# Print the calculated span values
printArray(ans, n)