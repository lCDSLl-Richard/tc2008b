import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Astro import Astro

astros: list[Astro] = []

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

FOVY = 60.0
ZNEAR = 0.01
ZFAR = 500.0

EYE_X = 10.0
EYE_Y = 10.0
EYE_Z = 10.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0

X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500
Z_MIN = -500
Z_MAX = 500


def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    glBegin(GL_LINES)

    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(X_MIN, 0.0, 0.0)
    glVertex3f(X_MAX, 0.0, 0.0)

    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, Y_MIN, 0.0)
    glVertex3f(0.0, Y_MAX, 0.0)

    # Z axis in blue
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, Z_MIN)
    glVertex3f(0.0, 0.0, Z_MAX)

    glEnd()
    glLineWidth(1.0)


def Init():
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: ejes 3D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, SCREEN_WIDTH / SCREEN_HEIGHT, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

    astros.append(Astro(4.0, 0.5, [0.0, 0.0, 1.0], 1.0))
    astros.append(Astro(5.5, 0.7, [0.0, 1.0, 1.0], 0.4))
    astros.append(Astro(7.0, 0.6, [0.3, 0.6, 0.5], 2.6))
    astros.append(Astro(13, 1.2, [1, 0.4, 0], 0.8))

    astros[0].addMoon(Astro(1.5, 0.1, [1.0, 1.0, 1.0], 1.0))
    astros[1].addMoon(Astro(1.5, 0.1, [1.0, 1.0, 1.0], 1.7))
    astros[3].addMoon(Astro(2, 0.4, [1, 1, 1], 0.5))


sun = Astro(0, 2, [1, 0, 0], 1)

Init()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glShadeModel(GL_FLAT)

    # Axis
    sun.draw()

    for astro in astros:
        astro.draw()

    pygame.display.flip()
    pygame.time.wait(20)

pygame.quit()
