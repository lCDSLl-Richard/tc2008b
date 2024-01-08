import pygame
from random import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective


vertices = (
    (1, -1, 1),
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, 1),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, -1),
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
)


def lerp_color(color1, color2, t):
    return (
        color1[0] + t * (color2[0] - color1[0]),
        color1[1] + t * (color2[1] - color1[1]),
        color1[2] + t * (color2[2] - color1[2]),
    )


def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    last_time = pygame.time.get_ticks()
    interval = 3000
    current_color = (random(), random(), random())
    target_color = (random(), random(), random())

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    quit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            pygame.quit()
                            quit()

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_time
        t = min(1, (elapsed_time / interval))
        current_color = lerp_color(current_color, target_color, t)
        glColor3f(*current_color)

        if current_time - last_time >= interval:
            target_color = (random(), random(), random())
            last_time = current_time

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
