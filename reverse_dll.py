# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    # get left and right end of list
    l, r = head, head

    # move to right
    while r.next:
        r = r.next

    # swap left and right data for each node
    while l is not r and l.prev is not r:
        temp = l.data
        l.data = r.data
        r.data = temp
        l = l.next
        r = r.prev

    return head