# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int,
                     list2: ListNode) -> ListNode:
    # Initialize an index to keep track of the current position in the list
    idx = 0

    # Initialize two pointers, head and final_list, to traverse list1
    final_list = head = list1

    # Move head pointer to the node just before the subarray to be removed (node a-1)
    while idx != a - 1:
      head = head.next
      idx += 1
    prev = head  # Store this node as prev, as it will be the node preceding the insertion point

    # Move head pointer to the node just after the subarray to be removed (node b+1)
    while idx != b + 1:
      head = head.next
      idx += 1
    next = head  # Store this node as next, as it will be the node succeeding the insertion point

    # Connect the previous node (prev) to the head of list2
    prev.next = list2
    head2 = list2  # Initialize a pointer to traverse list2

    # Move to the end of list2
    while head2.next:
      head2 = head2.next

    # Connect the end of list2 to the node succeeding the insertion point (next)
    head2.next = next

    # Return the head of the modified list1
    return final_list
