def findMergeNode(head1, head2):
    # create pointers
    pt1 = head1
    pt2 = head2

    # while the nodes are the the same
    while pt1 is not pt2:
        # if end of list 1 is reached
        if pt1.next is None:
            # pointer is the head of 2nd list
            pt1 = head2
        else:
            # move pointer to next node
            pt1 = pt1.next
        
        # if end of list 2 is reached
        if pt2.next is None:
            # 2nd pointer is the head of the 1st list
            pt2 = head1
        else:
            # move 2nd pointer to next node in list
            pt2 = pt2.next
    # return the value of 1st pointer, this is the intersecting node
    return pt1.data
