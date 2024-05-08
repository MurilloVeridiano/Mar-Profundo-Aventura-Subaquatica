import pygame
from configuracoes import LARGURA_JANELA, ALTURA_JANELA

class CenarioSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image_path), (LARGURA_JANELA, ALTURA_JANELA))
        self.rect = self.image.get_rect(x=position_x, y=0)
        self.velocity = -1  # Velocidade de movimento para a esquerda

    def update(self):
        self.rect.x += self.velocity
        # Reposiciona o sprite para o fim da fila se ele sair completamente da tela
        if self.rect.right < 0:
            # Calcula a nova posição baseada no número de sprites no grupo
            self.rect.x = self.rect.width * (len(self.groups()[0].sprites()) - 1)

class CenarioManager(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        # Criar e adicionar sprites de cenário
        for i in range(1, 5):
            sprite = CenarioSprite(f'Imagens/cenario{i}.png', LARGURA_JANELA * (i - 1))
            self.add(sprite)

    def update(self):
        super().update()  # Atualiza todos os sprites do grupo
        # Reorganiza os sprites conforme eles saem da tela para criar um loop contínuo
        sprites = sorted(self.sprites(), key=lambda x: x.rect.x)
        for i, sprite in enumerate(sprites):
            if sprite.rect.right < 0:
                sprite.rect.x = sprites[-1].rect.right


# Criação do gerenciador de cenários
gerenciador_cenarios = CenarioManager()


