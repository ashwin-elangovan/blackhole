# Basic stack operations
stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')
# stack.pop()
# stack.pop(0)


# Implement queue using stack
class MyQueue:

  def __init__(self):
    self.s1 = []
    self.s2 = []

  # Making enqueue costlier
  def push(self, key):
    while self.s1:
      self.s2.append(self.s1.pop())
    self.s1.append(key)
    while self.s2:
      self.s1.append(self.s2.pop())

  def pop(self):
    self.s1.pop()

  def peek(self):
    self.s1[-1]

  # Making dequeue costlier
  def push2(self, key):
    self.s1.append(key)

  def pop2(self):
    while self.s1:
      self.s2.append(self.s1.pop())
    self.s2.pop()
    while self.s2:
      self.s1.append(self.s2.pop())

  def peek2(self):
    return self.s1[0]

  def is_empty(self):
    return not self.s1 and not self.s2

  def items(self):
    for i in range(0, len(self.s1)):
      print(self.s1[i])


# val = MyQueue()
# val.push2(1)
# val.push2(2)
# val.push2(3)
# print(val.s1)
# val.pop2()
# print(val.s1)
# print(val.peek2())
# print(val.is_empty())
# val.items()

from collections import deque


# Implement stack using two queue (Dequeue operation is costly)
class MyStack1:

  def __init__(self):
    self.q1 = deque()
    self.q2 = deque()
    self._top = None

  def push(self, key):
    self.q1.append(key)
    self._top = key

  def pop(self):
    while len(self.q1) > 1:
      self._top = self.q1.popleft()
      self.q2.append(self._top)
    result = self.q1.popleft()
    self.q2, self.q1 = self.q1, self.q2
    return result

  def top(self):
    return self._top

  def empty(self):
    return len(self.q1) == 0


s = MyStack1()
s.push(1)
s.push(2)
s.push(3)
print(s.q1)
s.pop()
print(s.q1)

# Implement stack using single queue


class MyStack:

  def __init__(self):
    self.queue = None

    ## or ##
    # self.queue = deque()

  def push(self, key):
    q = deque()
    q.append(key)
    if self.queue:
      q.extend(self.queue)
    self.queue = q

    ### or ##
    # self.queue.appendleft(key)

  def pop(self):
    self.queue.popleft()

  def top(self):
    return self.queue[0]

  def empty(self):
    return not self.queue


# s = MyStack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.queue)
# s.pop()
# print(s.queue)


# Reverse a string using stacks
def strrev(string):
  s = []
  for i in string:
    s.append(i)
  rev = ''
  while s:
    rev += s.pop()
  return rev


print(strrev("Hello"))


# Balanced paranthesis
def balanced_paranthesis(brackets):
  s = []
  for char in brackets:
    if char == "(" or char == "[" or char == "{":
      s.append(char)
    else:
      current_char = s.pop()
      if (current_char == '('
          and char != ")") or (current_char == '['
                               and char != "]") or (current_char == '{'
                                                    and char != "}"):
        return False
  if s:
    return False
  return True


# print(balanced_paranthesis("([])"))


# Stockspan
# maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than its price on the given day.
def stockspan(prices):
  # Initialize the final arr
  final_arr = [0 for i in range(len(prices))]
  print(final_arr)
  # Temp stack to maintain indexes
  temp_stack = []
  # Add 0th element to the temp stack
  temp_stack.append(0)

  # Set default value for 1st element
  final_arr[0] = 1

  for i in range(1, len(prices)):
    # Pop out to find the biggest element to the left
    while len(temp_stack) > 0 and prices[temp_stack[-1]] <= prices[i]:
      temp_stack.pop()
    # If temp_stack is empty then all the left elements are lower than the current value
    if len(temp_stack) == 0:
      final_arr[i] = i + 1
    else:
      # Range from current element to the biggest element in the left
      final_arr[i] = (i - temp_stack[-1])
    temp_stack.append(i)
  return final_arr


# O(N). It seems more than O(N) at first look. If we take a closer look, we can observe that every element of the array is added and removed from the stack at most once.
print(stockspan([10, 4, 5, 90, 120, 80]))
