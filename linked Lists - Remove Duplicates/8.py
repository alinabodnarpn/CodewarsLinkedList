class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def remove_duplicates(head):
    if not head:
        return None
    current = head
    while current != None:
        if current.next and current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
