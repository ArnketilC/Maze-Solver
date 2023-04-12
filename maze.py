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
                    self.grid[i][j] = Node(i, j)
                    self.end = self.grid[i][j]
                    self.grid[i][j].name = "End"

        print(f"End: {self.end.x}, {self.end.y}")
        print(f"Start: {self.start.x}, {self.start.y}")
        print("I mapped everything")
        input()

    def __calculate_all_heuristic(self):
        """Calculate heuristic for all node in the range."""
        for line in self.grid:
            for node in line:
                if node.name != "End" and node.name != "B":
                    node.calculate_heuristic(self.end)
                print(f"Name:{node.name}, x:{node.x}, y:{node.y}, h:{node.heuristic}")

    def __check_adjacent_node(self, node) -> bool:
        """Check next other nodes."""
        cardinal = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for i, j in cardinal:  # Check all cardinal directions
            try:
                target_node = self.grid[node.x + i][node.y + j]
                if target_node.name != "End" and target_node.name != "B" and target_node.name != "Start":
                    # Skip if its the end, an obstacle or the start
                    if target_node not in self.checked_list:
                        # Check if the node was already check for adjacency
                        if target_node.heuristic == math.inf:  # Calculate heuristic if needed
                            target_node.calculate_heuristic(self.end)
                        self.checked_list.append(target_node)  # Add to the priority queue
                    # if target_node.step_cost >= node.step_cost:
                        # Change the cost to get to the target, if need be (not that usefull with step 1)
                        if node.last_node != target_node:
                            target_node.last_node = node
                            target_node.step_cost = node.step_cost
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
        # Sort the priority queue node base on the new heuristic
        # print("I Sort stuff")
        # print("list :")
        # for item in self.checked_list:
        #     print(f"{item.name}, {item.combine_heuristic}, {item.heuristic}")
        self.checked_list.sort(key=lambda x: x.combine_heuristic)  # , reverse=True)
        return False

    def __aStar(self, node) -> None:
        """A star solver."""
        found_endpoint = False
        skip = False
        last_node = ''
        number_of_check = 0
        while (found_endpoint is False):
            # Loop until found endpoint or dead end.
            for i, node in enumerate(self.checked_list):
                if node not in self.already_checked:
                    # print(f"cheking: {node.name}, x:{node.x}, y:{node.y}, ch:{node.combine_heuristic}")  # Check for double checking.
                    still_checking = True  # To deal with dead end.
                    # Check for adjacency.
                    found_endpoint = self.__check_adjacent_node(self.checked_list[i])
                    last_node = node
                    number_of_check += 1
                    break
                found_endpoint = False

            # Contition for dead end.
            if still_checking is False:
                found_endpoint = True
                skip = True
            else:
                still_checking = False
    
        if skip is False:  # If end found
            step_list = [self.end, last_node]
            while (last_node.name != 'Start'):
                # print(f"last_node.name, {last_node.x}, {last_node.y}")
                last_node = last_node.last_node
                step_list.append(last_node)
        if skip is True:  # If dead end
            return False

        print(number_of_check)
        return step_list

    def solve_w_AStar(self):
        """Solve the maze using the A* algorithm."""
        self.checked_list = []  # No suprise
        self.already_checked = []  # No suprise
        print(self.start.give_your_name())
        self.__check_adjacent_node(self.start)  # Check for the first adjancy
        solution = self.__aStar(self.checked_list[0])  # Start A* the first good adjancy
        if solution is not False:
            solution.reverse()  # Reverse list order for showing.
            for i, node in enumerate(solution):
                print(f"Step {i}: {node.give_your_name()} ")
        else:
            print("No solution found !")

    def __dij_check_adjacent_node(self, node, debug=0) -> bool:
        """Check next other nodes."""
        cardinal = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for i, j in cardinal:  # Check all cardinal directions
            try:
                target_node = self.grid[node.x + i][node.y + j]
                if target_node.name != "End" and target_node.name != "B" and target_node.name != "Start":
                    # Skip if its the end, an obstacle or the start
                    if target_node not in self.checked_list: 
                        # Check if the node was already check for adjacency
                        self.checked_list.append(target_node)  # Add to the priority queue
                        # print(f"{node.name}, {node.step_cost}")
                    # if target_node.step_cost >= node.step_cost+1:
                        # Change the cost to get to the target, if need be (not that usefull with step 1)
                        if node.last_node != target_node:
                            target_node.last_node = node
                            target_node.step_cost = node.step_cost +1
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
        # Sort the priority queue node base on the new heuristic
        self.checked_list.sort(key=lambda x: x.step_cost)  # , reverse=True)

        print("list :")
        for item in self.checked_list:
            print(f"{item.name}, {node.step_cost}")
        return False

    def __dijikstra(self, node):
        """Dijkstra solver."""
        found_endpoint = False
        skip = False
        last_node = ''
        number_of_check = 0
        while (found_endpoint is False):
            # Loop until found endpoint or dead end.
            for i, node in enumerate(self.checked_list):
                if node not in self.already_checked:  # Check for double checking.
                    still_checking = True  # To deal with dead end.
                    # Check for adjacency.
                    found_endpoint = self.__dij_check_adjacent_node(self.checked_list[i])
                    last_node = node
                    break
                found_endpoint = False
                number_of_check += 1
            # Contition for dead end.
            if still_checking is False:
                found_endpoint = True
                skip = True
            else:
                still_checking = False

        if skip is False:  # If end found
            step_list = [self.end, last_node]
            while (last_node.name != 'Start'):
                last_node = last_node.last_node
                step_list.append(last_node)
        if skip is True:  # If dead end
            return False
        print(number_of_check)
        return step_list

    def solve_w_Dijkstra(self):
        """Solve the maze using the Dijkstra algorithm"""
        self.checked_list = []  # No suprise
        self.already_checked = []  # No suprise
        self.__dij_check_adjacent_node(self.start)
        solution = self.__dijikstra(self.checked_list[0])  # Start A* the first good adjancy
        if solution is not False:
            solution.reverse()  # Reverse list order for showing.
            for i, node in enumerate(solution):
                print(f"Step {i}: {node.give_your_name()} ")
        else:
            print("No solution found !")
