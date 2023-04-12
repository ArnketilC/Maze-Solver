from maze import Maze
from time import time


def time_it(foo, *args, **kwargs):
    start = time()
    foo(*args, **kwargs)
    end = time()
    print(f"The function took {end-start} sec")


def main() -> None:
    maze = Maze('maze')
    maze.solve_w_AStar()
    print("End")


if __name__ == '__main__':
    main()
