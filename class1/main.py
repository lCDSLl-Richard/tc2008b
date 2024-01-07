import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Pyramid import Pyramid
from MatrixOp import MatrixOp

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# vc para el obser.
FOVY = 30.0
ZNEAR = 1.0
ZFAR = 500.0

# Variables para definir la posicion del observador
# gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
EYE_X = 10.0
EYE_Y = 10.0
EYE_Z = 10.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0

op = MatrixOp()
pyramid = Pyramid(op)


def Init():
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: 3D Pyramid")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, SCREEN_WIDTH / SCREEN_HEIGHT, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(EYE_X, EYE_Y, EYE_Z, CENTER_X, CENTER_Y, CENTER_Z, UP_X, UP_Y, UP_Z)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


Init()
done = False
while not done:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                done = True
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        done = True
                    case pygame.K_q:
                        op.rotateX(20)
                    case pygame.K_e:
                        op.rotateX(-20)
                    case pygame.K_w:
                        op.translate(0, 0.5, 0)
                    case pygame.K_s:
                        op.translate(0, -0.5, 0)
                    case pygame.K_d:
                        op.translate(0.5, 0, 0)
                    case pygame.K_a:
                        op.translate(-0.5, 0, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    pyramid.render()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
