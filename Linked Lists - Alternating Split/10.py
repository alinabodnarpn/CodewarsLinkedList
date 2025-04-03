class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List is empty or has only one node")
    
    list_one, list_two = None, None
    list_one_tail, list_two_tail = None, None
    current_node, is_list_one = head, True
    
    while current_node:
        if is_list_one:
            if not list_one:
                list_one = current_node
                list_one_tail = current_node
            else:
                list_one_tail.next = current_node
                list_one_tail = current_node
        else:
            if not list_two:
                list_two = current_node
                list_two_tail = current_node
            else:
                list_two_tail.next = current_node
                list_two_tail = current_node
        
        current_node = current_node.next
        is_list_one = not is_list_one
    
    if list_one_tail: list_one_tail.next = None
    if list_two_tail: list_two_tail.next = None
    
    return Context(list_one, list_two)