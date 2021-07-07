# Definition for singly-linked list.
class ListNode:
	 def __init__(self, val=0, next=None):
		 self.val = val
		 self.next = next

class Solution:
	def addTwoNumbers(self, l1, l2):
		"""
		"""
		output = ListNode(0)
		result = output
		# The first value:
		index_value = 0 #(l1.val + l2.val) % 10

		while l1 or l2:
			if l1:
				index_value += l1.val
				l1 = l1.next

			if l2:
				index_value += l2.val
				l2 = l2.next

			output.next = ListNode(index_value % 10)
			output = output.next

			if index_value > 9:
				index_value = 1
			else:
				index_value = 0

		if index_value:
			output.next = ListNode(index_value)

		return result.next


l1 = [1,2,3,4,5,6]
l2 = [2,3,4,5,6]
op = Solution()
print(op.addTwoNumbers(l1,l2))



"""
Runtime: 68 ms, faster than 75.91% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 41.77% of Python3 online submissions for Add Two Numbers.

"""