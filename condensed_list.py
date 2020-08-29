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

# traverse through linked list
    # store nodes in visited
    # if value already in visited, remove it
    # return new linked list

# use a set so that it doesn't store duplicate values
    # loop through ll and add nodes to the set
    # use pointers to keep track of nodes
    # return new list with current head

def condense(head):
    # Write your code here

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

'''
Time complexity is O(n) - will only take as much time as n number of nodes
Space complexity is O(n) - takes up as much space as the number of nodes in the linked list
'''