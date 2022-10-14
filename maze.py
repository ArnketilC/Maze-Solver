from typing import ParamSpecArgs
from node import Node
import math

maze = ''
class Maze:
    def __init__(self, file) -> None:
        """Init the maze"""
        self.grid = [[]]
        self.start = ""
        self.end = ""
        self.__fillGrid(file)
        self.__find_start_end()

    def __fillGrid(self, file) -> None:
        """Fille the array of characters"""
        with open(file) as f:
            grid = f.readlines()
            self.grid = [[*line.rstrip()] for line in grid]

    def __find_start_end(self) -> None:
        """Find start and end node"""
        for i, line in enumerate(self.grid):
            for j, value in enumerate(line):
                if value ==  "x":
                    self.grid[i][j] = Node(i,j,math.inf)
                    self.grid[i][j].name = "B"
                else :
                    self.grid[i][j] = Node(i,j)
                    self.grid[i][j].name = f"{i}{j}"
                if value == "$":
                    self.start = Node(i,j)
                    self.grid[i][j].name = "Start"
                elif value == "&":
                    self.end = Node(i, j)
                    self.grid[i][j].name = "End"

    def solve_w_AStar(self):
        for line in self.grid:
            for node in line:
                if node.name != "End" and node.name != "B":
                    node.calculate_heuristic(self.end)
                print(f"{node.name} ,{node.x}, {node.y}, {node.heuristic}")

    def solve_w_Dijkstra(self):
        pass 



