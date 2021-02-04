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
