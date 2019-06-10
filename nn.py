def dijsktra(graf, start, koniec):

    najkrotsza_droga = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != koniec:
        visited.add(current_node)
        destinations = graf.edges[current_node]
        weight_to_current_node = najkrotsza_droga[current_node][1]

        for next_node in destinations:
            weight = graf.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in najkrotsza_droga:
                najkrotsza_droga[next_node] = (current_node, weight)
            else:
                current_shortest_weight = najkrotsza_droga[next_node][1]
                if current_shortest_weight > weight:
                    najkrotsza_droga[next_node] = (current_node, weight)

        next_destinations = {node: najkrotsza_droga[node] for node in najkrotsza_droga if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = najkrotsza_droga[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path