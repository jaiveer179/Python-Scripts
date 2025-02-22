import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
JUMP_STRENGTH = 10
PLATFORM_WIDTH, PLATFORM_HEIGHT = 70, 10
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 100, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity_y = 0
        self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Check for ground collision
        if self.rect.y >= HEIGHT - PLAYER_HEIGHT:
            self.rect.y = HEIGHT - PLAYER_HEIGHT
            self.on_ground = True
            self.velocity_y = 0

        # Keep player within the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - PLAYER_WIDTH:
            self.rect.x = WIDTH - PLAYER_WIDTH

# Platform class
class Platform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.platforms = [Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), random.randint(0, HEIGHT - 50)) for _ in range(5)]
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.rect.x += 5
        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.player.update()

        # Check for platform collision
        for platform in self.platforms:
            if self.player.rect.colliderect(platform.rect) and self.player.velocity_y >= 0:
                if self.player.rect.bottom <= platform.rect.bottom + 10 and self.player.rect.bottom >= platform.rect.top:
                    self.player.rect.bottom = platform.rect.top
                    self.player.on_ground = True
                    self.player.velocity_y = 0

    def draw(self):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, self.player.rect)
        for platform in self.platforms:
            pygame.draw.rect(screen, GREEN, platform.rect)
        pygame.display.flip()

# Main function
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()