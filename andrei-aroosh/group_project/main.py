from libs.map import *


class Character:

    def __init__(self, name, cord):
        self.name = name
        self.cord = cord

    def change_cord(self):
        ui = input("Where would you like to move?: ")
        if ui.lower() == "up":
            self.cord=self.cord[0],self.cord[1]-1
        elif ui.lower() == "down":
            self.cord=self.cord[0],self.cord[1]+1
        elif ui.lower() == "left":
            self.cord=self.cord[0]-1,self.cord[1]
        elif ui.lower() == "right":
            self.cord=self.cord[0]+1,self.cord[1]


char = Character('Androosh', (0, 0))
game_map = Map(4, 4, 'X', char.cord)

game_map.show()

while True:
    char.change_cord()
    game_map.move_marker(char.cord)
    game_map.show()
