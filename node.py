import math

STEP = 1 # Maybe usefull for obstacles
class Node:
    def __init__(self, x, y, step=STEP) -> None:
        """Create a node object for calculation."""
        self.name = ""
        self.x = x
        self.y = y
        self.last_node = None
        self.heuristic = math.inf
        self.step_cost = math.inf
        self.combine_heuristic = math.inf

    def calculate_heuristic(self, endpoint) -> None:
        """Calculate heuristic based on the position of the end point."""
        self.heuristic = abs(self.x - endpoint.x + self.y - endpoint.x)

    def calculate_combine_heuristic(self) -> None:
        """Calculate heuristic and cost combinaison."""
        if self.last_node is not None:
            self.combine_heuristic = self.heuristic + self.step_cost
        else:
            self.combine_heuristic = self.heuristic

    def give_your_name(self) -> str:
        "Give it name and coordonates as string."
        return f"{self.name} @ coord: {self.x}, {self.y}"