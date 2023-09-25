import pygame
import cv2
import numpy as np

# Inicializa o Pygame
pygame.init()

# Configurando a janela do Pygame
largura, altura = 640, 480
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Captura da Webcam")

# Inicializa a webcam usando o OpenCV
captura = cv2.VideoCapture(0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            captura.release()
            pygame.quit()
            quit()

    # Captura um quadro da webcam
    ret, frame = captura.read()

    # Invertendo o quadro horizontalmente para exibir corretamente na janela Pygame
    frame = cv2.flip(frame, 1)

    # Convertendo o frame para Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # Exibe o quadro na janela Pygame
    janela.blit(frame, (0, 0))
    pygame.display.update()
