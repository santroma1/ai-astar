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




#map is 2 dimensional
def print_map(map, height, width):
    if type(map[0]) is not type([0,0]):
        print("Not a bidimensional array")
        return
    if not (type(map[0][0]) is type(" ") or type(map[0][0] is type(0))):
        print("Not a bidimensional array")
        return
    for x in range(height):
        for y in range(width):
            print(map[x][y], end=" ")
        print("")
    return


def search_a_star(map):
    pass


map1 = Map()
print_map(map1.manhattan, map1.height, map1.width)
print_map(map1.grid, map1.height, map1.width)

#search_a_star(map1)