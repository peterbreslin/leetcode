"""
– 	There is a singly-linked list head and we want to delete a node node in it.
– 	You are given the node to be deleted node, will not be given access to the first node of head.
– 	All the values of the linked list are unique, and it is guaranteed that the given node node is 
	not the last node in the linked list.
–	Delete the given node. Note that by deleting the node, we do not mean removing it from memory:

	– The value of the given node should not exist in the linked list.
	– The number of nodes in the linked list should decrease by one.
	– All the values before node should be in the same order.
	– All the values after node should be in the same order.

Custom testing:
For the input, you should provide the entire linked list head and the node to be given node. 
node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

====================================================================================================

SOLUTION:

A singly-linked list is a fundamental data structure used to organize and manage a sequence of 
elements. It consists of a series of nodes where each node contains two parts:

	– Data: The value or data held by the node.
	– Next: A reference or pointer to the next node in the sequence.

The FIRST node in the list is called the HEAD, and it serves as the ENTRY POINT to the list. 
The LAST node has its next pointer set to null (or None), indicating the END of the list.

To delete a node in a singly-linked list when you are given only a reference to that node and not 
the head of the list, you can follow a unique approach. Since you can't directly access the previous 
node to update its next pointer, you can instead copy the data from the next node to the given node 
and then delete the next node.

Step 1: Copy the Data – copy the data from the next node to the current node.
Step 2: Bypass the Next Node – set the next pointer of the current node to the next pointer of the 
		next node, effectively bypassing the next node.

This way, the current node takes on the value and pointer of the next node, and the next node is 
effectively removed from the list.

"""


# Definition for singly-linked list
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		# Ensure the node is not the last node
		if node.next is None:
			raise Exception("The given node is the last node and cannot be deleted.")
		
		# Step 1
		node.val = node.next.val
		
		# Step 2
		node.next = node.next.next


# Helper function to create a linked list from a list and return the head
def create_linked_list(elements):
	head = ListNode(elements[0])
	current = head
	for element in elements[1:]:
		current.next = ListNode(element)
		current = current.next
	return head

# Helper function to print the linked list
def print_linked_list(head):
	current = head
	while current:
		print(current.val, end=" -> ")
		current = current.next
	print("None")


# Example usage
if __name__ == "__main__":
	# Create a linked list: 1 -> 2 -> 3 -> 4
	head = create_linked_list([1, 2, 3, 4])

	# Suppose we want to delete the node with value 3
	node_to_delete = head.next.next  # This is the node with value 3

	# Print the linked list before deletion
	print("Before deletion:")
	print_linked_list(head)

	# Create an instance of Solution and delete the node
	solution = Solution()
	solution.deleteNode(node_to_delete)

	# Print the linked list after deletion
	print("After deletion:")
	print_linked_list(head)


		

