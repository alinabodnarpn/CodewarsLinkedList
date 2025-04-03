def swap_pairs(head):
    prev = None
    current = head
    head = current.next
    while current and current.next:
        next_node = current.next
        current.next = next_node.next
        next_node.next = current
        if prev:
            prev.next = next_node
        prev = current
        current = current.next
    return head
