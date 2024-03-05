#Name: Jack Chou
#Date: 10/22/2023
#Purpose: Create a body class for solar system

from cs1lib import *

class Body:
    # initialize instance variables
    def __init__(self, mass, x, y, v_x, v_y, picture):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y


        self.mass = mass
        self.image = load_image(picture)


    #updates the position of the planet
    def update_position(self, timestep):
        self.x = self.x + self.v_x * timestep
        self.y = self.y + self.v_y * timestep

    #updates the velocity of the planet
    def update_velocity(self, ax, ay, timestep):
        self.v_x = self.v_x + ax * timestep
        self.v_y = self.v_y + ay * timestep

    #draws the planet
    def draw(self, cx, cy, pixel_per_meter):
        draw_image(self.image, self.x * pixel_per_meter + cx, self.y * pixel_per_meter + cy)


