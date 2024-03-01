# Python program for the above approach
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class NodeOperation:
	# Function to add a new node
	def pushNode(self, head_ref, data_val):

		# Allocate node and put in the data
		new_node = Node(data_val)

		# Link the old list of the new node
		new_node.next = head_ref

		# move the head to point to the new node
		head_ref = new_node
		return head_ref

	# A utility function to print a given linked list
	def printNode(self, head):
		while (head != None):
			print('%d->' % head.data, end="")
			head = head.next
		print("NULL")

	''' Utility Function to find length of linked list '''

	def getLen(self, head):
		temp = head
		len = 0

		while (temp != None):
			len += 1
			temp = temp.next

		return len

	def printMiddle(self, head):
		if head != None:
			# find length
			len = self.getLen(head)
			temp = head

			# traverse till we reached half of length
			midIdx = len // 2
			while midIdx != 0:
				temp = temp.next
				midIdx -= 1

			# temp will be storing middle element
			print('The middle element is [ %d ]' % temp.data)


# Driver Code
head = None
temp = NodeOperation()
for i in range(5, 0, -1):
	head = temp.pushNode(head, i)
	temp.printNode(head)
	temp.printMiddle(head)

# This code is contributed by Tapesh(tapeshdua420)
