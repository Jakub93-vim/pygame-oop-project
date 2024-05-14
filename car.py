import pygame


class Car:

    def __init__(self, screen, color, player_pos):
        self.screen = screen
        self.color = color
        self.player_pos = player_pos

    def move_car(self, dt):

        rect = pygame.Rect(self.player_pos.x, self.player_pos.y, 20, 80)

        pygame.draw.rect(self.screen, self.color, rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt

class myRect(pygame.Surface):
