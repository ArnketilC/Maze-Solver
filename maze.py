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
        for i, j in cardinal: # Check all cardinal directions
            try:
                target_node = self.grid[node.x + i][node.y + j]
                if target_node.name != "End" and target_node.name != "B" and target_node.name != "Start":
                    # Skip if its the end, an obstacle or the start
                    if target_node not in self.checked_list: 
                        # Check if the node was already check for adjacency
                        self.checked_list.append(target_node) # Add to the list for sorting
                        if target_node.heuristic == math.inf : # Calculate heuristic if needed
                            target_node.calculate_heuristic(self.end)  
                    if target_node.step_cost >= node.step_cost + 1 :
                        # Change the cost to get to the target, if need be (not that usefull with step 1)
                        if node.last_node != target_node:
                            target_node.last_node = node
                            target_node.step_cost = node.step_cost + 1 
                            target_node.calculate_combine_heuristic()
                elif target_node.name == "End":
                    # If it's the end, no need to do previously mention steps
                    target_node.last_node = node
                    return True
                else:
                    count += 1
            except:
                pass
        
        # Add to the list of checked node
        self.already_checked.append(node)
        # Sort the list of node base on the new heuristic
        self.checked_list.sort(key=lambda x: x.combine_heuristic) #, reverse=True)

        return False
    
    def __aStar(self, node) -> None:
        """A star solver."""
        found_endpoint = False
        skip = False
        last_node = ''

        while (found_endpoint is False):
            # Loop until found endpoint or dead end.
            for i, node in enumerate(self.checked_list):
                if node not in self.already_checked: # Check for double checking.
                    still_checking = True # To deal with dead end.
                    # Check for adjacency.
                    found_endpoint = self.__check_adjacent_node(self.checked_list[i])
                    last_node = node
                    break
                found_endpoint = False

            # Contition for dead end.
            if still_checking is False:
                found_endpoint = True
                skip = True
            else:
                still_checking = False
           
        if skip is False: # If end found
            step_list = [self.end, last_node]
            while (last_node.name != 'Start'):
                last_node = last_node.last_node
                step_list.append(last_node)
        if skip is True: # If dead end
            return False

        return step_list

    def __dijikstra(node):
        """Check the node for path"""
        pass

    def solve_w_AStar(self):
        """Solve the maze using the A* algorithm."""
        self.__check_adjacent_node(self.start, debug=1) # Check for the first adjancy
        solution = self.__aStar(self.checked_list[0]) # Start A* the first good adjancy
        if solution is not False:
            solution.reverse() # Reverse list order for showing.
            for i, node in enumerate(solution):
                print(f"Step {i}: {node.give_your_name()} ")
        else:
            print("No solution found !")
   
    def solve_w_Dijkstra(self):
        """Under construction."""
        pass
