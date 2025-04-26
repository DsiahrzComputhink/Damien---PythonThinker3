import pygame
import random
import sys

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sols RNG")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 28)

# Rarity system: (name, chance %, color)
RARITIES = [
    ("Common", 60, (200, 200, 200)),
    ("Uncommon", 25, (50, 255, 50)),
    ("Rare", 10, (50, 100, 255)),
    ("Epic", 4, (190, 50, 255)),
    ("Legendary", 0.9, (255, 215, 0)),
    ("Mythical", 0.1, (255, 50, 50)),
]

def roll_rarity():
    roll = random.uniform(0, 100)
    total = 0
    for name, chance, color in RARITIES:
        total += chance
        if roll <= total:
            return name, color
    return "???", (0, 0, 0)

# Button setup
button_rect = pygame.Rect(WIDTH//2 - 75, HEIGHT - 100, 150, 50)

# Game state
current_rarity = "Click Roll"
rarity_color = (255, 255, 255)

# Main game loop
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                current_rarity, rarity_color = roll_rarity()

    # Draw rarity text
    text = font.render(current_rarity, True, rarity_color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    # Draw button
    pygame.draw.rect(screen, (70, 70, 70), button_rect)
    pygame.draw.rect(screen, (150, 150, 150), button_rect, 2)
    button_text = small_font.render("Roll", True, (255, 255, 255))
    button_rect_text = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_rect_text)

    pygame.display.flip()
    clock.tick(60)
