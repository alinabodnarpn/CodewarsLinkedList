class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def get_nth(node, index):
    if node is None:
        raise IndexError("Index out of range")
    current = node
    count = 0
    while current is not None:
        if count == index:
            return current
        current = current.next
        count += 1
    if current is None:
        raise Exception("Index out of range")

