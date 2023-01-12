import math


class Node:
    def __init__(self, x, y, step=1) -> None:
        """Create a node object for calculation."""
        self.name = ""
        self.x = x
        self.y = y
        self.last_node = None
        self.heuristic = math.inf
        self.step_cost = step  # Maybe usefull for obstacles
        self.combine_heuristic

    def calculate_heuristic(self, endpoint) -> None:
        """Calculate heuristic based on the position of the end point."""
        self.heuristic = abs(self.x - endpoint.x + self.y - endpoint.x)

    def calculate_combine_heuristic(self) -> None:
        """Calculate heuristic and cost combinaison."""
        if self.last_node is not None:
            self.combine_heuristic = self.heuristic + self.last_node.heuristic
        else:
            self.combine_heuristic = self.heuristic
