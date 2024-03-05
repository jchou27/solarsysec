#Name: Jack Chou
#Date: 10/22/2023
#Purpose: To create system class for the solar system

from body import *
from math import *

G = 6.67384e-11

class System:
    #Initializes the instance var body_list, like a list of planets
    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, n):
        axt = 0
        ayt = 0

        for planet in self.body_list:
            if self.body_list[n] != planet:
                dx = planet.x - self.body_list[n].x
                dy = planet.y - self.body_list[n].y
                r = sqrt((dx * dx) + (dy * dy))
                a = (G * planet.mass) / (r * r)

                ax = a * (dx / r)
                ay = a * (dy / r)

                axt = axt + ax
                ayt = ayt + ay

        return (axt, ayt)


    #updates both the position and velocity of all planets within body_list
    def update(self, timestep):
        for bodies1 in self.body_list:
            bodies1.update_position(timestep)

        for bodies2index in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(bodies2index)
            self.body_list[bodies2index].update_velocity(ax, ay, timestep)

    #draws all the planets within body_list
    def draw(self, cx, cy, pixels_per_meter):
        for bodies in self.body_list:
            bodies.draw(cx, cy, pixels_per_meter)










