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
        self.map = []

        self.generate()
        
    # 1 Generate is made, BUT NOT CALLED
    def generate(self):
        for i in range(1,self.height):
            self.map.append([])

        for i in self.map:
            for x in range(1,self.width):
                i.append([])

#2 Object is created
mymap = Map(width=3, height=3, player_marker='x', player_cord=(0, 0))
print(mymap.map)






        