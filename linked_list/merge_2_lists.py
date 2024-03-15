# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

  def mergeTwoLists(self, list1: Optional[ListNode],
                    list2: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize a temporary node and a final node to keep track of the merged list
    temp = final_node = ListNode()

    # Loop until either of the input lists becomes empty
    while list1 and list2:
      # Compare the values of the current nodes from both lists
      if list1.val < list2.val:
        # If the value in list1 is smaller, append it to the merged list
        temp.next = list1
        # Move to the next node in list1
        list1 = list1.next
      else:
        # If the value in list2 is smaller or equal, append it to the merged list
        temp.next = list2
        # Move to the next node in list2
        list2 = list2.next

      # Move the temporary node to the newly appended node
      temp = temp.next

    # If there are remaining nodes in either list, append them to the merged list
    if list1 or list2:
      temp.next = list1 if list1 else list2

    # Return the next node of the initial final node, which contains the merged list
    return final_node.next
