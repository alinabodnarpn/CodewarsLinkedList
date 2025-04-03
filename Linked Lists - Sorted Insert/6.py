class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    new_node = Node(data)

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
