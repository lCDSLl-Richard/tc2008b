from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np


class Cube:
    MIN_X = -20
    MAX_X = 20
    MIN_Z = -20
    MAX_Z = 20

    def __init__(self, position: list[float], speed: list[float]):
        self.vertex = [
            [-1, 0, -1],
            [-1, 0, 1],
            [1, 0, 1],
            [1, 0, -1],
            [-1, 2, -1],
            [-1, 2, 1],
            [1, 2, 1],
            [1, 2, -1],
        ]

        self.speed = np.array(speed)
        self.position = np.array(position)

    def render(self):
        glPushMatrix()
        glTranslate(*self.position)
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)

        # Bottom Face
        glVertex3fv(self.vertex[0])
        glVertex3fv(self.vertex[1])
        glVertex3fv(self.vertex[2])
        glVertex3fv(self.vertex[3])

        # Top Face
        glVertex3fv(self.vertex[4])
        glVertex3fv(self.vertex[5])
        glVertex3fv(self.vertex[6])
        glVertex3fv(self.vertex[7])

        # Left Face
        glVertex3fv(self.vertex[0])
        glVertex3fv(self.vertex[1])
        glVertex3fv(self.vertex[5])
        glVertex3fv(self.vertex[4])

        # Right Face
        glVertex3fv(self.vertex[2])
        glVertex3fv(self.vertex[3])
        glVertex3fv(self.vertex[7])
        glVertex3fv(self.vertex[6])

        # Front Face
        glVertex3fv(self.vertex[1])
        glVertex3fv(self.vertex[2])
        glVertex3fv(self.vertex[6])
        glVertex3fv(self.vertex[5])

        # Back Face
        glVertex3fv(self.vertex[0])
        glVertex3fv(self.vertex[3])
        glVertex3fv(self.vertex[7])
        glVertex3fv(self.vertex[4])

        glEnd()
        glPopMatrix()

    def update(self):
        self.position += self.speed

        x, _, z = self.position

        if x >= Cube.MAX_X - 1:
            self.position[0] = Cube.MAX_X - 1
            self.speed[0] *= -1

        if x <= Cube.MIN_X + 1:
            self.position[0] = Cube.MIN_X + 1
            self.speed[0] *= -1

        if z >= Cube.MAX_Z - 1:
            self.position[2] = Cube.MAX_Z - 1
            self.speed[2] *= -1

        if z <= Cube.MIN_Z + 1:
            self.position[2] = Cube.MIN_Z + 1
            self.speed[2] *= -1
