#Name: Jack Chou
#Date: 10/22/2023
#Purpose: to create the solar system driver
from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 370
WINDOW_HEIGHT = 370

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7 / 1e10

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE

def main():

    set_clear_color(0, 0, 0)
    clear()


    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    solar_system.update(TIMESTEP * TIME_SCALE)


sun = Body(1.98892e30, 0, 0, 0, 0, "picture/sun.png")
mercury = Body(0.33e24, -57.9e9, 0, 0, 47400, "picture/mercury.jpg")
venus = Body(4.87e24, -108.2e9, 0, 0, 35000, "picture/venus.jpg")
earth = Body(5.9736e24, -149.6e9, 0, 0, 29800, "picture/earth.jpg")
mars = Body(0.642e24, -228e9, 0, 0, 24140, "picture/mars.jpg")

solar_system = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE, height=400, width=400)





