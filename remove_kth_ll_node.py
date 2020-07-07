'''
Write function that received input head node of linked list and integer k
Remove kth node from end of ll and return head node of updated list
If k is longer than length of ll, ll should not be changed
'''

class Solution:
	def removeNthFromEnd(self, head, n):
		cur = head
		npre= head
		dis = 0
		count = 1

		while cur.next is not None:
			cur = cur.next
			count += 1
			dis += 1
		while dis > n:
			npre = npre.next
			dis -= 1
		if count <= n:
			return head.next
		npre.next = npre.next.next
		return head