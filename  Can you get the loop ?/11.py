def loop_size(node):
    visited_nodes = {}
    current_node = node
    position = 0
    while current_node:
        if current_node in visited_nodes:
            loop_start_position = visited_nodes[current_node]
            return position - loop_start_position

        visited_nodes[current_node] = position
        current_node = current_node.next
        position += 1
