# Complete the 'condense' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def condense(head):
    # Write your code here
    # traverse through linked list
    # store nodes in visited
    # if value already in visited, remove it
    # return new linked list

    prev = None
    cur = head
    visited = set()

    # loop through nodes
    while cur:
        # if the value of the cur node is in the set
        if cur.data in visited:
            # move pointers to next nodes
            prev.next = cur.next
        
        # add node values to visited set
        else:
            visited.add(cur.data)
            # move pointer to next node
            prev = cur

        cur = prev.next

    return head