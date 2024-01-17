import pygame
from pygame.locals import *

# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Se carga el archivo de la clase Cubo
from Cubo import Cubo
import numpy as np

screen_width = 500
screen_height = 500
# vc para el obser.
FOVY = 60.0
ZNEAR = 0.01
ZFAR = 900.0
# Variables para definir la posicion del observador
# gluLookAt(EYE_X,EYE_Y,EYE_Z,CENTER_X,CENTER_Y,CENTER_Z,UP_X,UP_Y,UP_Z)
eye_pos = np.array([300.0, 10, 300])
eye_look = np.array([-1.0, 0, 0])
orientation = [0, 1, 0]
# Variables para dibujar los ejes del sistema
X_MIN = -500
X_MAX = 500
Y_MIN = -500
Y_MAX = 500
Z_MIN = -500
Z_MAX = 500
# Dimension del plano
DimBoard = 200
# Variables para el control del observador
radius = 300
speed = 5

pygame.init()

# cubo = Cubo(DimBoard, 1.0)
cubos = []
ncubos = 50


def Axis():
    glShadeModel(GL_FLAT)
    glLineWidth(3.0)
    # X axis in red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(X_MIN, 0.0, 0.0)
    glVertex3f(X_MAX, 0.0, 0.0)
    glEnd()
    # Y axis in green
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, Y_MIN, 0.0)
    glVertex3f(0.0, Y_MAX, 0.0)
    glEnd()
    # Z axis in blue
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, Z_MIN)
    glVertex3f(0.0, 0.0, Z_MAX)
    glEnd()
    glLineWidth(1.0)


def move_f():
    global eye_pos, eye_look, orientation, speed
    eye_pos += eye_look * speed

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def move_b():
    global eye_pos, eye_look, orientation, speed
    eye_pos -= eye_look * speed

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def move_r():
    global eye_pos, eye_look, orientation, speed
    rad = math.radians(90)
    aux = eye_look @ np.array(
        [
            [math.cos(rad), 0, math.sin(rad)],
            [0, 1, 0],
            [-math.sin(rad), 0, math.cos(rad)],
        ]
    )
    eye_pos += aux * speed

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def move_l():
    global eye_pos, eye_look, orientation, speed
    rad = math.radians(-90)
    aux = eye_look @ np.array(
        [
            [math.cos(rad), 0, math.sin(rad)],
            [0, 1, 0],
            [-math.sin(rad), 0, math.cos(rad)],
        ]
    )
    eye_pos += aux * speed

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def rotate_r():
    global eye_pos, eye_look, orientation, speed
    rad = math.radians(speed / 2)
    eye_look @= np.array(
        [
            [math.cos(rad), 0, math.sin(rad)],
            [0, 1, 0],
            [-math.sin(rad), 0, math.cos(rad)],
        ]
    )

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def move_u():
    global eye_pos, eye_look, orientation, speed
    eye_pos += np.array([0, speed, 0])
    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def move_d():
    global eye_pos, eye_look, orientation, speed
    eye_pos += np.array([0, -speed, 0])
    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def rotate_l():
    global eye_pos, eye_look, orientation, speed
    rad = math.radians(-speed / 2)
    eye_look @= np.array(
        [
            [math.cos(rad), 0, math.sin(rad)],
            [0, 1, 0],
            [-math.sin(rad), 0, math.cos(rad)],
        ]
    )

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def reset_pos():
    global eye_pos, eye_look, orientation, speed
    eye_pos = np.array([100.0, 10, 0])
    eye_look = np.array([-1.0, 0, 0])

    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)


def Init():
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("OpenGL: cubos")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOVY, screen_width / screen_height, ZNEAR, ZFAR)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*eye_pos, *(eye_pos + eye_look), *orientation)
    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    for _ in range(ncubos):
        cubos.append(Cubo(DimBoard, 1.0))


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Axis()
    # Se dibuja el plano gris
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    # Se dibuja cubos
    for obj in cubos:
        obj.draw()
        obj.update()


done = False
Init()
while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_f()
    if keys[pygame.K_d]:
        move_r()
    if keys[pygame.K_s]:
        move_b()
    if keys[pygame.K_a]:
        move_l()
    if keys[pygame.K_e]:
        rotate_r()
    if keys[pygame.K_q]:
        rotate_l()
    if keys[pygame.K_SPACE]:
        move_u()
    if keys[pygame.K_LCTRL]:
        move_d()
    if keys[pygame.K_r]:
        reset_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
