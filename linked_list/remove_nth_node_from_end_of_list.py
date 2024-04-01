# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def removeNthFromEnd(self, head: Optional[ListNode],
                       n: int) -> Optional[ListNode]:
    # Initialize two pointers, fast and slow, both starting from the head of the linked list.
    fast = slow = head

    # Move the fast pointer n steps forward to create a gap of n nodes between fast and slow pointers.
    for i in range(n):
      fast = fast.next

    # If fast reaches the end of the list (i.e., fast becomes None), it indicates that the node to be removed is the head itself.
    # In such a case, return the next node after the head as the new head of the list.
    if not fast:
      return head.next

    # Move both fast and slow pointers until fast reaches the last node of the list.
    # At this point, slow will be pointing to the node just before the node to be removed.
    while fast.next:
      fast, slow = fast.next, slow.next

    # Skip the node to be removed by adjusting the next pointer of the node before it.
    slow.next = slow.next.next

    # Return the head of the modified linked list.
    return head
