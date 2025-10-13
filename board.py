import pygame
import config
import os


class GameBoard:
    def __init__(self, screen):
        self.screen = screen

        # 🔹 Load hình bàn cờ (hỗ trợ cả PNG và JPG)
        if os.path.exists("assets/board.png"):
            self.board_img = pygame.image.load("assets/board.png").convert_alpha()
        else:
            self.board_img = pygame.image.load("assets/board.jpg").convert()

        # 🔹 Chỉnh kích thước ảnh bàn cờ theo cấu hình
        self.board_img = pygame.transform.scale(
            self.board_img, (config.BOARD_WIDTH, config.BOARD_HEIGHT)
        )

        # 🔹 Font hiển thị
        self.font = pygame.font.SysFont("SimHei", 50)  # Font hỗ trợ chữ Trung / Việt

    # ==============================================================
    #                        VẼ BÀN CỜ
    # ==============================================================
    def draw_board(self, black_pieces, red_pieces, valid_moves, current_turn=None):
        # Nền tổng thể (viền ngoài)
        self.screen.fill(config.BG_COLOR)

        # Vẽ ảnh bàn cờ
        self.screen.blit(self.board_img, (config.BOARD_X, config.BOARD_Y))

        # Vẽ các nước đi hợp lệ (chấm tròn xanh)
        for move in valid_moves:
            pygame.draw.circle(
                self.screen,
                config.BLUE,
                (
                    config.BOARD_X + move[0] * config.CELL_SIZE,
                    config.BOARD_Y + move[1] * config.CELL_SIZE,
                ),
                config.CELL_SIZE // 6,
            )

        # Vẽ quân đen
        for pos, text in black_pieces.items():
            self.draw_piece(pos[0], pos[1], config.BLACK, text, config.BLACK_BG)

        # Vẽ quân đỏ
        for pos, text in red_pieces.items():
            self.draw_piece(pos[0], pos[1], config.RED, text, config.RED_BG)

        # Hiển thị lượt đi
        if current_turn:
            self.draw_turn_indicator(current_turn)

        pygame.display.flip()

    # ==============================================================
    #                        VẼ QUÂN CỜ
    # ==============================================================
    def draw_piece(self, x, y, color, text, bg_color):
        # 🔹 Tính tọa độ trung tâm quân cờ (giao điểm)
        center = (
            config.BOARD_X + x * config.CELL_SIZE,
            config.BOARD_Y + y * config.CELL_SIZE,
        )

        # Nền quân cờ
        pygame.draw.circle(self.screen, bg_color, center, config.CELL_SIZE // 2 - 5)
        pygame.draw.circle(self.screen, color, center, config.CELL_SIZE // 2 - 2, 3)

        # Ký hiệu quân cờ
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        self.screen.blit(text_surface, text_rect)

    # ==============================================================
    #                     HIỂN THỊ LƯỢT ĐI
    # ==============================================================
    def draw_turn_indicator(self, current_turn):
        color = config.RED if current_turn == "red" else config.BLACK
        text = f"Lượt: {'ĐỎ' if current_turn == 'red' else 'ĐEN'}"
        turn_surface = self.font.render(text, True, color)
        self.screen.blit(
            turn_surface,
            (config.BOARD_X, config.BOARD_Y + config.BOARD_HEIGHT + 30),
        )
