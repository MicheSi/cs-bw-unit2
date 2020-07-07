# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        # only 1 list
        if len(lists) == 1:
            return lists[0]
        # find middle node
        mid = len(lists) // 2
        
        # use recursion to traverse each side of the array
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        
        return self.merge2Lists(l, r)
        
    def merge2Lists(self, l, r):
        temp = cur = ListNode(0)
        
        while l and r:
            # compare node values, if left is smaller, assign next node to left
            if l.val < r.val:
                cur.next = l
                # move to next node in left list
                l = l.next
            # right is larger, so assign next to right node
            else:
                cur.next = r
                r = r.next
            # move to next node
            cur = cur.next
            
        cur.next = l or r
            
        return temp.next