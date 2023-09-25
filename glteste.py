import pygame as pg
import moderngl as mgl
import sys
from model import *

class GraphicsEngine:
    def __init__(self, win_size=(640, 480)):
        # Inicializando os módulos do Pygame
        pg.init()
        # Tamanho da janela
        self.WIN_SIZE = win_size
        # Setando os atributos para OpenGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Criando o contexto do OpenGL
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Detectando e usando o contexto existente do OpenGL
        self.ctx = mgl.create_context()
        # Criando um objeto para ajudar a fazer um track no tempo
        self.clock = pg.time.Clock()
        # Cena
        self.scene = Triangle(self)

    # Função para checar os eventos
    def check_events(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    # Método de renderização
    def render(self):
        # Limpando o framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # Renderizar as cenas
        self.scene.render()
        # Trocando os buffers
        pg.display.flip()

    # Método run
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()

