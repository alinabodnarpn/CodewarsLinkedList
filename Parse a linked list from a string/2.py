class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == "None":
        return None

    nodes = s.split(" -> ")[:-1]
    head = Node(int(nodes[0])) if nodes else None
    current = head
    for value in nodes[1:]:
        current.next = Node(int(value))
        current = current.next
    return head
