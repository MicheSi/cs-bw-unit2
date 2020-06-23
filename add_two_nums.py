'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize head
        head = l1
        # initialize carry to sum / 10
        carry = (l1.val + l2.val) // 10
        # create new node with digit value of sum % 10
        l1.val = (l1.val + l2.val) % 10
        # loop through lists while there is a next node
        while l1.next and l2.next:
            # add value of next node to carry
            carry += l1.next.val
            carry += l2.next.val
            # create new node with value and update carry
            l1.next.val = carry % 10
            carry = carry // 10
            #set next nodes
            l1 = l1.next
            l2 = l2.next
        # if no next node in l1, set next node to 1st node in l2    
        if l1.next is None:
            l1.next = l2.next
        # while l1 has next node    
        while l1.next:
            # set carry to value of next node
            carry += l1.next.val
            # create new node with value and update carry
            l1.next.val = carry % 10
            carry = carry // 10
            # set pointer to next node
            l1 = l1.next
            
        if carry > 0:
            l1.next = ListNode(carry)
            
        return head