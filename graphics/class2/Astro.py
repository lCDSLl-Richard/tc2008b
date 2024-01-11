from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Astro:
    def __init__(self, dist: float, esc: float, color: list[float], v_ang: float):
        self.deg = 0.0
        self.dist = dist
        self.esc = esc
        self.color = color.copy()
        self.v_ang = v_ang
        self.sphere = gluNewQuadric()
        self.moons: list[Astro] = []

    def update(self):
        self.deg += self.v_ang
        if self.deg >= 360.0:
            self.deg = 0

    def draw(self):
        glPushMatrix()
        glColor3fv(self.color)
        glRotatef(self.deg, 0.0, 1.0, 0.0)
        glTranslatef(self.dist, 0.0, 0.0)
        glScalef(self.esc, self.esc, self.esc)
        glRotatef(-90, 1, 0, 0.0)
        gluSphere(self.sphere, 1.0, 16, 16)
        glRotatef(90, 1, 0, 0)

        for moon in self.moons:
            moon.draw()

        glPopMatrix()
        self.update()

    def addMoon(self, moon: "Astro"):
        self.moons.append(moon)
