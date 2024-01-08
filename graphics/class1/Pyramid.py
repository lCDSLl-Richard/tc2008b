import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from MatrixOp import MatrixOp


class Pyramid:
    def __init__(self, op: MatrixOp):
        self.op = op
        self.points = np.array(
            [
                [1.0, 0.0, 1.0, 1.0],
                [1.0, 0.0, -1.0, 1.0],
                [-1.0, 0.0, -1.0, 1.0],
                [-1.0, 0.0, 1.0, 1.0],
                [0.0, 3.0, 0.0, 1.0],
            ]
        )

    def render(self):
        pointsR = self.points.copy()
        self.op.apply(pointsR)
        glBegin(GL_QUADS)
        for point in pointsR:
            glVertex3f(point[0], point[1], point[2])
        glEnd()

        glBegin(GL_LINES)
        for i in range(0, 4):
            glVertex3f(pointsR[i][0], pointsR[i][1], pointsR[i][2])
            glVertex3f(pointsR[4][0], pointsR[4][1], pointsR[4][2])
        glEnd()
