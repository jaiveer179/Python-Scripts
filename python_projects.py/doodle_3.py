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
PLATFORM_SPEED = 2

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Fonts
font = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 100, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity_y = 0
        self.on_ground = False
        self.score = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.y >= HEIGHT - PLAYER_HEIGHT:
            self.rect.y = HEIGHT - PLAYER_HEIGHT
            self.on_ground = True
            self.velocity_y = 0

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - PLAYER_WIDTH:
            self.rect.x = WIDTH - PLAYER_WIDTH

# Platform class
class Platform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    def update(self):
        self.rect.y += PLATFORM_SPEED

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.platforms = [Platform(random.randint(0, WIDTH - PLATFORM_WIDTH), HEIGHT - (i * 100)) for i in range(6)]
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.game_started = False  # Flag to track game state

    def run(self):
        while self.running:
            self.handle_events()
            if self.game_started:
                self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_started:
                    x, y = event.pos
                    if start_button.collidepoint(x, y):
                        self.game_started = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.rect.x += 5
        if keys[pygame.K_SPACE]:
            self.player.jump()
        if keys[pygame.K_r] and self.game_over:
            self.restart()

    def update(self):
        if not self.game_over:
            self.player.update()
            for platform in self.platforms:
                platform.update()
                if platform.rect.y > HEIGHT:
                    platform.rect.y = random.randint(-50, -10)
                    platform.rect.x = random.randint(0, WIDTH - PLATFORM_WIDTH)
                    self.player.score += 1
                if self.player.rect.colliderect(platform.rect) and self.player.velocity_y >= 0:
                    if self.player.rect.bottom <= platform.rect.bottom + 10 and self.player.rect.bottom >= platform.rect.top:
                        self.game_over = True
                        return
            if self.player.rect.top <= HEIGHT // 3:
                for platform in self.platforms:
                    platform.rect.y += abs(self.player.velocity_y)
                self.player.rect.y += abs(self.player.velocity_y)
            if self.player.rect.y >= HEIGHT:
                self.game_over = True

    def draw(self):
        screen.fill(WHITE)
        if self.game_started:
            pygame.draw.rect(screen, BLUE, self.player.rect)
            for platform in self.platforms:
                pygame.draw.rect(screen, GREEN, platform.rect)
            score_text = font.render(f"Score: {self.player.score}", True, RED)
            screen.blit(score_text, (10, 10))
            if self.game_over:
                game_over_text = font.render("Game Over! Press R to Restart", True, RED)
                screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        else:
            pygame.draw.rect(screen, BLACK, start_button)
            text = font.render("Start Game", True, WHITE)
            screen.blit(text, (WIDTH // 2 - 50, HEIGHT // 2 - 10))
        pygame.display.flip()

    def restart(self):
        self.__init__()
        self.game_started = True

# Create start button
start_button = pygame.Rect(WIDTH // 2- 60, HEIGHT // 2 - 20, 120, 40)

# Main function
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()