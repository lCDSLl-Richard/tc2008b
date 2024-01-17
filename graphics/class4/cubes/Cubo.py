# Autor: Ivan Olmos Pineda
# Cargamos las bibliotecas de OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import random
import math
import numpy as np


class Cube:
    cubes: list["Cube"] = []

    def __init__(self, dim, vel):
        # vertices del cubo
        self.points = np.array(
            [
                [-1.0, -1.0, 1.0],
                [1.0, -1.0, 1.0],
                [1.0, -1.0, -1.0],
                [-1.0, -1.0, -1.0],
                [-1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0],
                [1.0, 1.0, -1.0],
                [-1.0, 1.0, -1.0],
            ]
        )

        self.dimBoard = dim
        # Se inicializa una posicion aleatoria en el tablero
        self.position = [
            random.randint(-self.dimBoard, self.dimBoard),
            5.0,
            random.randint(-self.dimBoard, self.dimBoard),
        ]
        # Se inicializa un vector de direccion aleatorio
        self.direction = [random.random(), 5.0, random.random()]
        # Se normaliza el vector de direccion
        m = math.sqrt(self.direction[0] ** 2 + self.direction[2] ** 2)
        self.direction[0] /= m
        self.direction[2] /= m
        # Se cambia la maginitud del vector direccion
        self.direction[0] *= vel
        self.direction[2] *= vel
        self.radius = math.sqrt(3) * 4
        Cube.cubes.append(self)

    def update(self):
        new_x = self.position[0] + self.direction[0]
        new_z = self.position[2] + self.direction[2]

        # detecc de que el objeto no se salga del area de navegacion
        if abs(new_x) <= self.dimBoard:
            self.position[0] = new_x
        else:
            self.direction[0] *= -1.0
            self.position[0] += self.direction[0]

        if abs(new_z) <= self.dimBoard:
            self.position[2] = new_z
        else:
            self.direction[2] *= -1.0
            self.position[2] += self.direction[2]

        for cube in Cube.cubes:
            if cube is self:
                continue

            dist_x = cube.position[0] - self.position[0]
            dist_z = cube.position[2] - self.position[2]

            dist = np.linalg.norm([dist_x, dist_z])

            if dist <= self.radius + cube.radius:
                self.direction[0] *= -1
                self.direction[2] *= -1
                break

    def drawFaces(self):
        glBegin(GL_QUADS)
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])
        glVertex3fv(self.points[3])

        glVertex3fv(self.points[4])
        glVertex3fv(self.points[5])
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[7])

        glVertex3fv(self.points[0])
        glVertex3fv(self.points[1])
        glVertex3fv(self.points[5])
        glVertex3fv(self.points[4])

        glVertex3fv(self.points[1])
        glVertex3fv(self.points[2])
        glVertex3fv(self.points[6])
        glVertex3fv(self.points[5])

        glVertex3fv(self.points[2])
        glVertex3fv(self.points[3])
        glVertex3fv(self.points[7])
        glVertex3fv(self.points[6])

        glVertex3fv(self.points[3])
        glVertex3fv(self.points[0])
        glVertex3fv(self.points[4])
        glVertex3fv(self.points[7])
        glEnd()

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glScaled(5, 5, 5)
        glColor3f(1.0, 1.0, 1.0)
        self.drawFaces()
        glPopMatrix()
