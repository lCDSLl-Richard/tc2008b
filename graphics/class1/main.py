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
EYE_X = 20.0
EYE_Y = 20.0
EYE_Z = 20.0
CENTER_X = 0
CENTER_Y = 0
CENTER_Z = 0
UP_X = 0
UP_Y = 1
UP_Z = 0


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


def main(ex):
    op = MatrixOp()
    pyramid = Pyramid(op)

    if ex == "1":
        op.rotate(15, 0.5, 0.5, 0)
        op.translate(3.0, -5.0, 1.0)
        op.scale(1.5, 1.0, 1.5)
    elif ex == "2":
        op.scale(1.5, 1.0, 1.5)
        op.rotate(15, 0.5, 0.5, 0)
        op.translate(3.0, -5.0, 1.0)

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
                        case pygame.K_x:
                            op.scale(2, 2, 2)
                        case pygame.K_z:
                            op.scale(0.5, 0.5, 0.5)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        Axis()
        glColor3f(1, 1, 1)
        pyramid.render()

        pygame.display.flip()
        pygame.time.wait(100)

    pygame.quit()


if __name__ == "__main__":
    try:
        ex = sys.argv[1]
    except:
        ex = ""
    main(ex)
