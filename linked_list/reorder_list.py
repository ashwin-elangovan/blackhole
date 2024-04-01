# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def reorderList(self, head: Optional[ListNode]) -> None:
    """
        Do not return anything, modify head in-place instead.
        """
    # Step 1: Find the middle of the linked list
    slow, fast = head, head

    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    curr = slow.next

    while curr:
      nextt = curr.next
      curr.next = prev
      prev = curr
      curr = nextt
    slow.next = None

    # Step 3: Merge the original and reversed halves of the linked list
    head1, head2 = head, prev
    while head1 and head2:
      nxt1 = head1.next
      nxt2 = head2.next

      head1.next = head2
      head1 = nxt1

      head2.next = head1
      head2 = nxt2
