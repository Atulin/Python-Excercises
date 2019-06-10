import math


class Point:
    name: str
    x: int
    y: int

    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name} [{self.x}, {self.y}]"

    def __repr__(self):
        return str(self)


# Calculate distance between two points
def distance(a: Point, b: Point):
    diff_x = abs(a.x - b.x)
    diff_y = abs(a.y - b.y)
    return math.sqrt(pow(diff_x, 2) + pow(diff_y, 2))


graph = [
    Point("A", 1, 2),
    Point("B", 3, 1),
    Point("C", 3, 6),
    Point("D", 6, 7),
    Point("E", 5, 2)
]

start = "E"


for i in graph:
    for j in graph:
        print(f"{i.name} to {j.name}: {distance(i, j)}")
