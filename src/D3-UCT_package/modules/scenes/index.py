import pygame
import setting

class game_buttons:
    def game_option_buttons(self, surface):
        pygame.draw.rect(surface, setting.table_accent_colour, (75, 0, 300, 50), 0, 0, 0, 0, 5, 5)
        pygame.draw.rect(surface, setting.table_accent_colour, (450, 0, 300, 50), 0, 0, 0, 0, 5, 5)
        pygame.draw.rect(surface, setting.table_accent_colour, (825, 0, 300, 50), 0, 0, 0, 0, 5, 5)

        pygame.draw.rect(surface, setting.white, (75, -5, 300, 55), 2, 0, 0, 0, 5, 5)
        pygame.draw.rect(surface, setting.white, (450, -5, 300, 55), 2, 0, 0, 0, 5, 5)
        pygame.draw.rect(surface, setting.white, (825, -5, 300, 55), 2, 0, 0, 0, 5, 5)
        
GB = game_buttons()

class game_button_hover:
    def game_option_buttons_hover(self):
        mousePos_x, mousePos_y = pygame.mouse.get_pos()
        if 75 <= mousePos_x <= 375 and 0 <= mousePos_y <= 50:
            print("trigger")
        elif 450 <= mousePos_x <= 750 and 0 <= mousePos_y <= 50:
            print("trigger")
        elif 825 <= mousePos_x <= 1125 and 0 <= mousePos_y <= 50:
            print("trigger")

GBH = game_button_hover()
