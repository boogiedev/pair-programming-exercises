# This is a group project that Andrei and Aroosh will be working on, below will be a set of tasks that you guys are required to collaborate and work on. Be sure to divide the work and communicate

'''
You guys are tasked with making a map object, required functionality will be as follows:

- Object has to be initialized with width, height, player_marker, and current location of player
- Map object should have methods that allow the current location of player to change as well as to update the map with the current position (shown by the marker)

- METHODS (these are some suggested methods)
    - .update() this function will 'update' the map with current player coordinates shown via player_marker
    - .show() this function will print the map out in a user readable way
    - .move_marker(cord=(1, 0)) this function will move the player marker to the designated coordinate

Example script:

map = Map(width=3, height=3, player_marker='x', player_cord=(0, 0))
map.show()

x - -
- - -
- - -

^ result of map.show()

map.move_marker(cord=(1,0))
map.update()
map.show()

- x -
- - -
- - -

^ result of map.show()
'''

# 1 Class is made, BUT not called
class Map:

    # 1 init is made, BUT NOT CALLED
    def __init__(self, width, height, player_marker, player_cord):
        # 2 Object init, OBJECT IS CREATED
        self.width = width
        self.height = height
        self.player_marker = player_marker
        self.player_cord = player_cord
        self.grid = []
        self.generate()

    # 1 Generate is made, BUT NOT CALLED
    def generate(self):
        self.grid = []
        for _ in range(self.height):
            row = ['-' for _ in range(self.width)]
            self.grid.append(row)

        player_x, player_y = self.player_cord[0], self.player_cord[1]
        self.grid[player_y][player_x] = "X"

    def move_marker(self, coordinate):
        self.player_cord = coordinate
        self.generate()

    def show(self):
        pretty_map = """"""
        for row in self.grid:
            str_row = " ".join(row)
            pretty_map += str_row + "\n"
        print(pretty_map)



#2 Object is created
mymap = Map(width=3, height=3, player_marker='x', player_cord=(0, 0))
mymap.show()

mymap.move_marker(coordinate=(0, 1))

print("\n")
mymap.show()
print(mymap.grid)
