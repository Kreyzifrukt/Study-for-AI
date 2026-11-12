import pygame
import random

# Инициализация
pygame.init()

# Настройки поля
WIDTH, HEIGHT = 450, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
MINES_COUNT = 15

# Цвета
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont('Arial', 24, bold=True)


class Minesweeper:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.flags = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.mines = []
        self.game_over = False
        self.won = False
        self.first_click = True

    def place_mines(self, start_x, start_y):
        positions = []
        while len(self.mines) < MINES_COUNT:
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            # Не ставим мину там, где был первый клик
            if (x, y) not in self.mines and (x, y) != (start_x, start_y):
                self.mines.append((x, y))
                self.grid[y][x] = -1

        # Считаем цифры вокруг мин
        for x, y in self.mines:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.grid[ny][nx] != -1:
                        self.grid[ny][nx] += 1

    def reveal(self, x, y):
        if self.game_over or self.flags[y][x] or self.revealed[y][x]:
            return

        if self.first_click:
            self.place_mines(x, y)
            self.first_click = False

        self.revealed[y][x] = True

        if self.grid[y][x] == -1:
            self.game_over = True
            return

        if self.grid[y][x] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        self.reveal(nx, ny)

        # Проверка на победу
        revealed_count = sum(row.count(True) for row in self.revealed)
        if revealed_count == (GRID_SIZE ** 2 - MINES_COUNT):
            self.won = True

    def toggle_flag(self, x, y):
        if not self.revealed[y][x]:
            self.flags[y][x] = not self.flags[y][x]

    def draw(self):
        screen.fill(GRAY)
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if self.revealed[y][x]:
                    pygame.draw.rect(screen, WHITE, rect)
                    if self.grid[y][x] == -1:
                        pygame.draw.circle(screen, BLACK, rect.center, CELL_SIZE // 3)
                    elif self.grid[y][x] > 0:
                        text = font.render(str(self.grid[y][x]), True, BLUE if self.grid[y][x] < 3 else RED)
                        screen.blit(text, text.get_rect(center=rect.center))
                else:
                    pygame.draw.rect(screen, DARK_GRAY, rect)
                    if self.flags[y][x]:
                        pygame.draw.polygon(screen, RED,
                                            [(rect.left + 10, rect.bottom - 10), (rect.right - 10, rect.bottom - 10),
                                             (rect.centerx, rect.top + 10)])

                pygame.draw.rect(screen, BLACK, rect, 1)

        # Текст состояния
        msg = "ИГРАЕМ"
        if self.game_over: msg = "БУМ! (R - рестарт)"
        if self.won: msg = "ПОБЕДА! (R - рестарт)"
        status_text = font.render(msg, True, BLACK)
        screen.blit(status_text, (20, HEIGHT - 40))


def main():
    game = Minesweeper()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                gx, gy = mx // CELL_SIZE, my // CELL_SIZE

                if gy < GRID_SIZE:
                    if event.button == 1:  # ЛКМ
                        game.reveal(gx, gy)
                    elif event.button == 3:  # ПКМ
                        game.toggle_flag(gx, gy)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = Minesweeper()

        game.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()