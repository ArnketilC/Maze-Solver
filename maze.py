from typing import ParamSpecArgs
from node import Node
import math

maze = ''


class Maze:
    def __init__(self, file) -> None:
        """Init the maze."""
        self.grid = [[]]
        self.start = ""
        self.end = ""
        self.__fillGrid(file)
        self.__find_start_end()
        self.path = []
        self.checked_list = []
        self.already_checked = []

    def __fillGrid(self, file) -> None:
        """Fille the array of characters."""
        with open(file) as f:
            grid = f.readlines()
            self.grid = [[*line.rstrip()] for line in grid]

    def __find_start_end(self) -> None:
        """Find start and end node."""
        for i, line in enumerate(self.grid):
            for j, value in enumerate(line):
                if value == "x":
                    self.grid[i][j] = Node(i, j, math.inf)
                    self.grid[i][j].name = "B"
                else:
                    self.grid[i][j] = Node(i, j)
                    self.grid[i][j].name = f"Node {i}{j}"
                if value == "$":
                    self.grid[i][j] = Node(i, j)
                    self.start = self.grid[i][j]
                    self.start.sp_cost = 0
                    self.grid[i][j].name = "Start"
                elif value == "&":
                    self.grid[i][j]  = Node(i, j)
                    self.end = self.grid[i][j]
                    self.grid[i][j].name = "End"

    def __calculate_all_heuristic(self):
        """Calculate heuristic for all node in the range."""
        for line in self.grid:
            for node in line:
                if node.name != "End" and node.name != "B":
                    node.calculate_heuristic(self.end)
                print(f"Name:{node.name}, x:{node.x}, y:{node.y}, h:{node.heuristic}")


    def __check_adjacent_node(self, node, debug=0) -> bool:
        """Check next other nodes."""
        cardinal = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for i, j in cardinal:
            try:
                target_node = self.grid[node.x + i][node.y + j]
                if target_node.name != "End" and target_node.name != "B" and target_node.name != "Start":

                    if target_node not in self.checked_list:
                        self.checked_list.append(target_node)
                        if target_node.heuristic == math.inf:
                            target_node.calculate_heuristic(self.end)    
                    if target_node.step_cost >= node.step_cost + 1 :
                        if node.last_node != target_node:
                            target_node.last_node = node
                            target_node.step_cost = node.step_cost + 1 
                            target_node.calculate_combine_heuristic()

                elif target_node.name == "End":
                    target_node.last_node = node
                    return True
                else:
                    count += 1
            except:
                pass
        
        # Sort everything in the list
        self.already_checked.append(node)
        self.checked_list.sort(key=lambda x: x.combine_heuristic) #, reverse=True)

        return False
    
    def __aStar(self, node) -> None:
        """A star solver."""
        found_endpoint = False
        skip = False
        last_node = ''
        count = 0
        while (found_endpoint is False):
            for i, node in enumerate(self.checked_list):
                if node not in self.already_checked:
                    still_checking = True   
                    found_endpoint = self.__check_adjacent_node(self.checked_list[i])
                    last_node = node
                    break
                found_endpoint = False

            if still_checking is False:
                found_endpoint = True
                skip = True
            else:
                still_checking = False
           
        if skip is False:
            step_list = [self.end, last_node]
            while (last_node.name != 'Start'):
                last_node = last_node.last_node
                step_list.append(last_node)
        if skip is True:
            return False

        return step_list

    def __dijikstra(node):
        """Check the node for path"""
        pass

    def solve_w_AStar(self):
        """Solve the maze using the A* algorithm."""
        print(self.start.name)
        self.__check_adjacent_node(self.start, debug=1)
        solution = self.__aStar(self.checked_list[0])
        if solution is not False:
            solution.reverse()
            for i, node in enumerate(solution):
                print(f"Step {i}: {node.give_your_name()} ")
        else:
            print("No solution found !")
   
    def solve_w_Dijkstra(self):
        """Under construction."""
        pass
