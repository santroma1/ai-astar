import random


class Map:

    def find_manhattan(self):
        pass

    def choose_start(self):
        pass

    def choose_goal(self):
        pass


    def __init__(self):
        self.height = 6
        self.width = 6
        self.grid = [[0,1,0,0,0,0],
                     [0,1,0,0,0,0],
                     [0,1,0,1,0,0],
                     [0,1,0,0,0,0],
                     [0,1,0,1,0,0],
                     [0,0,0,1,1,0]]
        self.cost = 1
        self.movement_arrows = ["^", "<", "v", ">"]
        self.movements = [[1,0], [0,-1], [-1,0], [0,1]]
                
        self.start = [0,0]

        self.goal = [5,5]

        self.manhattan = [[0,1,2,3,4,5],
                          [1,2,3,4,5,6],
                          [2,3,4,5,6,7],
                          [3,4,5,6,7,8],
                          [4,5,6,7,8,9],
                          [5,6,7,8,9,10]]

        




#grid is 2 dimensional
def print_map(grid):
    if type(grid[0]) is not type([0,0]):
        print("Not a bidimensional array")
        return
    if not (type(grid[0][0]) is type(" ") or type(grid[0][0] is type(0))):
        print("Not a bidimensional array")
        return
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(grid[x][y], end=" ")
        print("")
    return


def search_a_star(map):
    visited = [[False for j in range(map.width)] for i in range(map.height)]
    visited[map.begin[0]][map.begin[1]] = True
    steps = [[-1 for j in range(map.width)] for i in range(map.height)]
    action = [[-1 for j in range(map.width)] for i in range(map.height)]
    path = [["-" for j in range(map.width)] for i in range(map.height)]

    x = map.start[0]
    y = map.start[1]
    h = map.manhattan[x][y]
    g = 0
    f = g + h

    expansion_list = [[f,g,x,y]]

    found = False
    give_up = False
    count = 0

    x2 = 0
    y2 = 0

    return steps, path

    

    


map1 = Map()
print_map(map1.manhattan)
print("")
print_map(map1.grid)
print("")


steps, path = search_a_star(map1)
print_map(steps)
print("")
print_map(path)