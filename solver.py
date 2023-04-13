from maze import Maze
from time import time


def time_it(foo):
    """Timing of function."""
    def wrapper(*args, **kwargs):
        start = time()
        foo(*args, **kwargs)
        end = time()
        print(f"The function took {end-start} sec")
    return wrapper


@time_it
def a_star(maze):
    """Simple wraper for A star."""
    print("Solving with A*.")
    maze.solve_w_AStar()
    print("Solved with A*.")

@time_it 
def dijkstra(maze):
    """Simple wraper for Dijkstra."""
    print("Solving with Dijkstra.")
    maze.solve_w_Dijkstra()
    print("Solving with Dijkstra.")

def main() -> None:
    # maze = Maze('maze')
    # maze = Maze('maze_2')
    maze = Maze('assets/maze_2')
    # dijkstra(maze)
    print("-----")
    a_star(maze)
    print("End")

if __name__ == '__main__':
    main()
