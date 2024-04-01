# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

  def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Initialize two pointers, slow and fast, both starting from the head of the linked list.
    slow, fast = head, head

    # Loop until either fast pointer reaches the end of the list (fast is None) or fast's next node is None.
    while (fast and fast.next):
      # Move slow pointer one step forward.
      slow = slow.next
      # Move fast pointer two steps forward.
      fast = fast.next.next

      # If at any point, slow and fast pointers meet, it indicates a cycle in the linked list.
      if (slow == fast):
        # Return True, indicating that the linked list has a cycle.
        return True

    # If the loop completes without finding any cycle, return False, indicating no cycle in the linked list.
    return False
