def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False

def has_cycle(head):
    visited = {}
    while head:
        visited[head]=1
        if visited.get(head.next,0) != 0:
            return True
        head = head.next
    return False