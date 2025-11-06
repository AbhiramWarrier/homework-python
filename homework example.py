import pygame
pygame init()
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

display_surface = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.display.set_caption("my first game screen")

pygame.draw.rect(surface, color, pygame.Rect(60, 60, 90, 90))

rect.center = (screen_width // 2, screen_height // 2)
font = pygame.font.Font(36, None)
text_surface = font.render("this is a rectangle", True, (0, 0, 0))

background_color = (0, 0, 0)
