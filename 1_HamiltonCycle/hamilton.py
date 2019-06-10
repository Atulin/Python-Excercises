import math


# Class defining the point
class Point:
    name: str
    x: int
    y: int

    # Constructor
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    # Conversion to string
    def __str__(self):
        return f"{self.name} [{self.x}, {self.y}]"

    # Print
    def __repr__(self):
        return str(self)


# Calculate distance between two points
def distance(a: Point, b: Point):
    diff_x = abs(a.x - b.x)
    diff_y = abs(a.y - b.y)
    return math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))


# Calculate the total length
def total_length(graph: list):
    total = 0
    for i in range(1, len(graph) - 1):
        total += distance(graph[i-1], graph[i])

    return total


# Calculate the path
def hamilton(graph: list, starting_point_name: str) -> list:
    graph = shuffle(graph, starting_point_name)
    next_point = graph[0]
    visited = [next_point]

    # Go over all of the points in the graph
    i = 0
    while len(graph) > 1:
        print(i)
        point = visited[i]
        graph.remove(point)
        shortest_distace = math.inf
        potential_next = None

        # Go over the remaining points
        for pn in graph:
            if distance(point, pn) < shortest_distace:
                shortest_distace = distance(point, pn)
                potential_next = pn

        next_point = potential_next
        visited.append(next_point)
        i += 1

    visited.append(visited[0])

    return visited


# Shuffle the selected starting point to the beginning of the array
def shuffle(points_array: list, starting_point_name: str) -> list:
    start_point: Point = next((x for x in points_array if x.name == starting_point_name), None)
    points_array.remove(start_point)
    out: list = [start_point]
    for p in points_array:
        out.append(p)
    return out


#################################
#                               #
#           EXECUTION           #
#                               #
#################################

# Define the graph
graph = [
    Point("A", 1, 2),
    Point("B", 3, 1),
    Point("C", 3, 6),
    Point("D", 6, 7),
    Point("E", 5, 2)
]

# Select the starting point
start = "E"

h = hamilton(graph, start)
print(h)
print(total_length(h))
