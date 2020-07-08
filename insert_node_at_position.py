class SinglyLinkedListNode:
    pass

def insertNodeAtPosition(head, data, position):
    n=head
    if position==0:
        head=SinglyLinkedListNode(data)
        head.next=n
    else:
        for i in range(position-1):
            n=n.next
        n_next=n.next
        n.next=SinglyLinkedListNode(data)
        n.next.next=n_next
    return head