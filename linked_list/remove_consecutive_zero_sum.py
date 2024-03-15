# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def removeZeroSumSublists(self,
                            head: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node to handle edge cases
    dummy_node = ListNode(0)
    dummy_node.next = head

    # Initialize a dictionary to store prefix sums and their corresponding nodes
    prefix_sum = {
      0: dummy_node
    }  # If sum is 0 in between then dummy_node.next will be current_idx

    curr_sum = 0
    # Calculate prefix sums and store the last node for each prefix sum
    while head:
      curr_sum += head.val
      prefix_sum[
        curr_sum] = head  # It'll store the last position of the prefix sum
      head = head.next

    # Reset head and prefix for the next iteration
    head = dummy_node
    prefix = 0

    # Traverse the list again to remove zero-sum subarrays
    while head:
      prefix += head.val
      # Update the next pointer of the current node to skip zero-sum subarrays
      head.next = prefix_sum[
        prefix].next  # Since we are jumping pointers, we don't have to worry about the same prefix sum again
      head = head.next

    return dummy_node.next
