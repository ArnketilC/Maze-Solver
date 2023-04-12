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
    maze.solve_w_AStar()


def main() -> None:
    maze = Maze('maze')
    a_star(maze)

    # print("End")


if __name__ == '__main__':
    main()
