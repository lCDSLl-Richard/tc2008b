import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Cube import Cube

from random import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# vc para el obser.
FOVY = 30.0
ZNEAR = 1.0
ZFAR = 500.0

# Variables para definir la posicion del observador
# gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X = 50.0
EYE_Y = 50.0
EYE_Z = 50.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0

PLAIN_MIN_X = -20
PLAIN_MAX_X = 20
PLAIN_MIN_Z = -20
PLAIN_MAX_Z = 20


def Init():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: 3D Cubes")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, SCREEN_WIDTH / SCREEN_HEIGHT, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def Axis():
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)

    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-500, 0.0, 0.0)
    glVertex3f(500, 0.0, 0.0)

    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 500, 0.0)
    glVertex3f(0.0, -500, 0.0)

    # Z axis in blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 500)
    glVertex3f(0.0, 0.0, -500)

    glEnd()
    glLineWidth(0.1)


def Plain():
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3f(128 / 255, 128 / 255, 128 / 255)
    glVertex3f(PLAIN_MIN_X, 0, PLAIN_MIN_Z)
    glVertex3f(PLAIN_MIN_X, 0, PLAIN_MAX_Z)
    glVertex3f(PLAIN_MAX_X, 0, PLAIN_MAX_Z)
    glVertex3f(PLAIN_MAX_X, 0, PLAIN_MIN_Z)
    glEnd()
    glPopMatrix()


cubes = [
    Cube([0.0, 0, 0], [-1.0, 0, 1]),
    Cube([0.0, 0, 0], [2.0, 0, -1]),
    Cube([0.0, 0, 0], [10.0, 0, 0.2]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
    Cube([0.0, 0, 0], [random(), 0, random()]),
]

Init()
done = False
while not done:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1, 1, 1)
    Axis()
    Plain()

    for cube in cubes:
        cube.render()
        cube.update()

    pygame.display.flip()
    pygame.time.wait(50)
