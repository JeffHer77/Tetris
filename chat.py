import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
BOARD_WIDTH, BOARD_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Colores
COLORS = [
    (0, 0, 0),       # Fondo
    (255, 0, 0),     # Rojo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (255, 255, 0),   # Amarillo
    (255, 165, 0),   # Naranja
    (128, 0, 128),   # Púrpura
]

# Formas de las piezas
SHAPES = [
    [[1, 1, 1, 1]],                # I
    [[1, 1, 1], [0, 1, 0]],        # T
    [[1, 1], [1, 1]],              # O
    [[0, 1, 1], [1, 1, 0]],        # S
    [[1, 1, 0], [0, 1, 1]],        # Z
    [[1, 0, 0], [1, 1, 1]],        # L
    [[0, 0, 1], [1, 1, 1]],        # J
]

class Tetris:
    def __init__(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.current_pos = [0, BOARD_WIDTH // 2 - 1]

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = COLORS[random.randint(1, len(COLORS) - 1)]
        lista = [shape, color]
        return lista  # Devolver la forma como lista

    def rotate(self):
        self.current_piece[0] = [list(row) for row in zip(*self.current_piece[0][::-1])]

    def valid_move(self, offset):
        piece = self.current_piece[0]
        for r in range(len(piece)):
            for c in range(len(piece[r])):
                if piece[r][c]:
                    x = self.current_pos[0] + r + offset[0]
                    y = self.current_pos[1] + c + offset[1]
                    if x < 0 or x >= BOARD_HEIGHT or y < 0 or y >= BOARD_WIDTH or (x >= 0 and self.board[x][y]):
                        return False
        return True

    def lock_piece(self):
        piece = self.current_piece[0]
        for r in range(len(piece)):
            for c in range(len(piece[r])):
                if piece[r][c]:
                    self.board[self.current_pos[0] + r][self.current_pos[1] + c] = self.current_piece[1]
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = self.new_piece()
        self.current_pos = [0, BOARD_WIDTH // 2 - 1]
        if not self.valid_move((0, 0)):
            self.reset()

    def clear_lines(self):
        lines_to_clear = [i for i in range(BOARD_HEIGHT) if all(self.board[i])]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * BOARD_WIDTH)

    def reset(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

def draw_board(screen, board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c]:
                pygame.draw.rect(screen, board[r][c], (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    tetris = Tetris()
    fall_time = 0
    fall_speed = 500  # milisegundos
    running = True

    while running:
        screen.fill(COLORS[0])
        fall_time += clock.get_time()
        if fall_time >= fall_speed:
            if tetris.valid_move((1, 0)):
                tetris.current_pos[0] += 1
            else:
                tetris.lock_piece()
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and tetris.valid_move((0, -1)):
                    tetris.current_pos[1] -= 1
                if event.key == pygame.K_RIGHT and tetris.valid_move((0, 1)):
                    tetris.current_pos[1] += 1
                if event.key == pygame.K_DOWN and tetris.valid_move((1, 0)):
                    tetris.current_pos[0] += 1
                if event.key == pygame.K_UP:
                    original_piece = [row[:] for row in tetris.current_piece[0]]  # Copia profunda de la pieza
                    tetris.rotate()
                    if not tetris.valid_move((0, 0)):
                        tetris.current_piece[0] = original_piece

        draw_board(screen, tetris.board)
        piece_shape = tetris.current_piece[0]
        for r in range(len(piece_shape)):
            for c in range(len(piece_shape[r])):
                if piece_shape[r][c]:
                    pygame.draw.rect(screen, tetris.current_piece[1],
                                     ((tetris.current_pos[1] + c) * BLOCK_SIZE,
                                      (tetris.current_pos[0] + r) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
