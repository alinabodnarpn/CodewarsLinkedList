class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise Exception("Source list is empty")
    new_source = source.next
    source.next = dest
    new_dest = source
    return Context(new_source, new_dest)
