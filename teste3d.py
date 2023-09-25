import pygame
from pygame.locals import *
import OpenGL.GL as GL
from OpenGL.GLUT import *

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Objeto 3D com Pygame")

# Função para desenhar um cubo 3D
def desenhar_cubo():
    GL.glBegin(GL.GL_QUADS)
    GL.glVertex3f(-1, -1, -1)
    GL.Vertex3f(1, -1, -1)
    GL.glVertex3f(1, 1, -1)
    GL.glVertex3f(-1, 1, -1)

    GL.glVertex3f(-1, -1, 1)
    GL.glVertex3f(1, -1, 1)
    GL.glVertex3f(1, 1, 1)
    GL.glVertex3f(-1, 1, 1)

    GL.glVertex3f(-1, -1, -1)
    GL.glVertex3f(1, -1, -1)
    GL.glVertex3f(1, -1, 1)
    GL.glVertex3f(-1, -1, 1)

    GL.glVertex3f(-1, 1, -1)
    GL.glVertex3f(1, 1, -1)
    GL.glVertex3f(1, 1, 1)
    GL.glVertex3f(-1, 1, 1)

    GL.glVertex3f(-1, -1, -1)
    GL.glVertex3f(-1, 1, -1)
    GL.glVertex3f(-1, 1, 1)
    GL.glVertex3f(-1, -1, 1)

    GL.glVertex3f(1, -1, -1)
    GL.glVertex3f(1, 1, -1)
    GL.glVertex3f(1, 1, 1)
    GL.glVertex3f(1, -1, 1)
    GL.glEnd()


# Loop Principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

    desenhar_cubo()

    pygame.display.flip()
    pygame.time.wait(10)