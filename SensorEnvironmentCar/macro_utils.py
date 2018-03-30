import pygame
from pygame.color import THECOLORS

import pymunk
from pymunk.vec2d import Vec2d
from pymunk.pygame_util import DrawOptions
import time

#Environment Macros
WIDTH = 1000
HEIGHT = 600
BG_COLOR = THECOLORS['black']
SENSORS_COLOR = THECOLORS['white']
ALARM_COLOR = THECOLORS['red']
FLAGS = pygame.DOUBLEBUF

# Unit Macros
UNIT_X = WIDTH/4        # Unit starting point - x value
UNIT_Y = HEIGHT/1.5     # Unit starting point - y value
UNIT_R = 20             # Unit dimensions - radius(circle type)

# Sensor Macros
DRAW_START = UNIT_R + 10
DRAW_LENGTH = 100
DRAW_STOP = DRAW_START + DRAW_LENGTH
COLL_THRESH = -1.0

OBSERVATION_SPACE = 5
ACTION_SPACE = 4

DRAWING = True

ACTION_NAMES = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}