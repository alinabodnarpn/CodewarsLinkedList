class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    if not node:
        return "None"
    return f"{node.data} -> {stringify(node.next)}"
