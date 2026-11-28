import pygame
import setting

# Variables
game_button_colour1 = setting.table_accent_colour
game_button_colour2 = setting.table_accent_colour
game_button_colour3 = setting.table_accent_colour

game_button_colours = [game_button_colour1, game_button_colour2, game_button_colour3]

def game_option_buttons_hover():
    global game_button_colour1, game_button_colour2, game_button_colour3, game_button_colours
    mousePos_x, mousePos_y = pygame.mouse.get_pos()
    if 75 <= mousePos_x <= 375 and 0 <= mousePos_y <= 50:
        if game_button_colour1 == setting.table_hover_colour:
            pass
        else:
            game_button_colour1 = setting.table_hover_colour
    else:
        game_button_colour1 = setting.table_accent_colour
            
    if 450 <= mousePos_x <= 750 and 0 <= mousePos_y <= 50:
        if game_button_colour2 == setting.table_hover_colour:
            pass
        else:
            game_button_colour2 = setting.table_hover_colour
    else:
        game_button_colour2 = setting.table_accent_colour

    if 825 <= mousePos_x <= 1125 and 0 <= mousePos_y <= 50:
        if game_button_colour3 == setting.table_hover_colour:
            pass
        else:
            game_button_colour3 = setting.table_hover_colour
    else:
        game_button_colour3 = setting.table_accent_colour

def game_option_buttons(surface):
    pygame.draw.rect(surface, game_button_colour1, (75, 0, 300, 50), 0, 0, 0, 0, 5, 5)
    pygame.draw.rect(surface, game_button_colour2, (450, 0, 300, 50), 0, 0, 0, 0, 5, 5)
    pygame.draw.rect(surface, game_button_colour3, (825, 0, 300, 50), 0, 0, 0, 0, 5, 5)

    pygame.draw.rect(surface, setting.white, (75, -5, 300, 55), 2, 0, 0, 0, 5, 5)
    pygame.draw.rect(surface, setting.white, (450, -5, 300, 55), 2, 0, 0, 0, 5, 5)
    pygame.draw.rect(surface, setting.white, (825, -5, 300, 55), 2, 0, 0, 0, 5, 5)
