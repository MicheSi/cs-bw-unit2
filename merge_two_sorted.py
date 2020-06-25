'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if both ll exist
        if l1 and l2:
            # check values of 1st node in each list
            # put the smaller value on the left
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # if there is a next node, use recursion to check through the other nodes
            if l1.next:
                return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
                # no more nodes to check, so return that node followed by 2nd ll
            else:
                return ListNode(l1.val, l2)
        # if linked list doesn't exist, return the other one
        elif not l1:
            return l2
        elif not l2:
            return l1