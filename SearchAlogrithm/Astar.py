# link ref: https://brilliant.org/wiki/a-star-search/

from queue import PriorityQueue

# The Manhattan Distance Heuristic
def ManhattanDistance(cell1, cell2) -> int:
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1 - x2) + abs(y1 - y2)

def a_star(mapMaze, start=None):

    # tmp set start is (5,5)
    if start == None:
        start = (5,5)

    g_score = {cell:float('inf') for cell in mapMaze.keys()}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in mapMaze.keys()}
    f_score[start] = ManhattanDistance(start, (1,1))
    
    # make a openList (priority queue)
    open = PriorityQueue()
    while not open.empty():
        if start == (1,1):
            break



if __name__ == '__main__':

    # implement maze in Picture3.png
    maze = {(1,1):{'R': 1, 'T':0, 'L': 0, 'B': 1},
            (1,2):{'R': 1, 'T':0, 'L': 1, 'B': 0},
            (1,3):{'R': 1, 'T':0, 'L': 1, 'B': 1},
            (1,4):{'R': 0, 'T':0, 'L': 1, 'B': 1},
            (1,5):{'R': 0, 'T':0, 'L': 0, 'B': 1},
            (2,1):{'R': 1, 'T':1, 'L': 0, 'B': 0},
            (2,2):{'R': 1, 'T':0, 'L': 1, 'B': 1},
            (2,3):{'R': 0, 'T':1, 'L': 1, 'B': 0},
            (2,4):{'R': 1, 'T':1, 'L': 0, 'B': 0},
            (2,5):{'R': 0, 'T':1, 'L': 1, 'B': 1},
            (3,1):{'R': 1, 'T':0, 'L': 0, 'B': 1},
            (3,2):{'R': 1, 'T':1, 'L': 1, 'B': 0},
            (3,3):{'R': 1, 'T':0, 'L': 1, 'B': 0},
            (3,4):{'R': 1, 'T':0, 'L': 1, 'B': 1},
            (3,5):{'R': 0, 'T':1, 'L': 1, 'B': 0},
            (4,1):{'R': 1, 'T':1, 'L': 0, 'B': 1},
            (4,2):{'R': 1, 'T':0, 'L': 1, 'B': 0},
            (4,3):{'R': 1, 'T':0, 'L': 1, 'B': 1},
            (4,4):{'R': 1, 'T':1, 'L': 1, 'B': 0},
            (4,5):{'R': 1, 'T':0, 'L': 1, 'B': 1},
            (5,1):{'R': 1, 'T':1, 'L': 0, 'B': 0},
            (5,2):{'R': 1, 'T':0, 'L': 1, 'B': 0},
            (5,3):{'R': 1, 'T':1, 'L': 1, 'B': 0},
            (5,4):{'R': 1, 'T':0, 'L': 1, 'B': 0},
            (5,5):{'R': 0, 'T':1, 'L': 1, 'B': 0}}
    # g_score = {cell:float('inf') for cell in maze.keys()}
    # print(len(g_score))