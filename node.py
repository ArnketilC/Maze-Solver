import math


class Node:
    def __init__(self, x, y, step=1) -> None:
        """Create a node object for calculation."""
        self.name = ""
        self.x = x
        self.y = y
        self.last_step = None
        self.heuristic = math.inf
        self.step = step  # Maybe usefull for obstacles
        self.cost = step

    def calculate_heuristic(self, endpoint) -> None:
        """Calculate euristic based on the position of the end point."""
        self.heuristic = abs(self.x - endpoint.x + self.y - endpoint.x)
