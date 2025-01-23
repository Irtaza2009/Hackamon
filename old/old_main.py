import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
import pygame
import time
import math
import random
from old_Hackamon import Hackamon

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

gameState = "Menu"

menu_font = bitmap_font.load_font("fonts/PixelifySans-Regular-12px.bdf")

menu_background = displayio.OnDiskBitmap("assets/Menu-BG.bmp")
menu_bg_sprite = displayio.TileGrid(menu_background, pixel_shader=menu_background.pixel_shader)

splash.append(menu_bg_sprite)

menu_box_sheet = displayio.OnDiskBitmap("assets/Menu-Box-Spritesheet.bmp")


 # test leaderboard data
menu_options = [
    {"text": "Time", "unselected_tile": 0, "selected_tile": 4},
    {"text": "Dice Roll", "unselected_tile": 1, "selected_tile": 5},
    {"text": "Coin Flip", "unselected_tile": 2, "selected_tile": 6},
    {"text": "Hackamon", "unselected_tile": 3, "selected_tile": 7},
]

menu_box_sprites = []
menu_box_options = []
current_selection = 0

for i, option in enumerate(menu_options):
    x = 14
    y = 5 + (i * 30)
    
    menu_box_sprite = displayio.TileGrid(menu_box_sheet,
                                            pixel_shader=menu_box_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=100,
                                            tile_height=25,
                                            default_tile=option["unselected_tile"],
                                            x=x,
                                            y=y)
    option_label = label.Label(
        menu_font, text=option["text"], color=0x7a8af0, anchor_point=(0, 0), anchored_position=(x + 5, y + 7)
    )

    menu_box_sprites.append(menu_box_sprite)
    menu_box_options.append(option_label)


    splash.append(menu_box_sprite)
    splash.append(option_label)

def update_menu_selection():
    for i, menu_box in enumerate(menu_box_sprites):
        if i == current_selection:
            menu_box[0] = menu_options[i]["selected_tile"]
        else:
            menu_box[0] = menu_options[i]["unselected_tile"]

def handle_selection():
    global gameState
    if current_selection == 0:
        print("Time")
    elif current_selection == 1:
        print("Dice Roll")
    elif current_selection == 2:
        print("Coin Flip")
    elif current_selection == 3:
        print("Hackamon")
        splash.pop()
        Hackamon_Game = Hackamon(display, splash)
        Hackamon_Game.main
        gameState = "Hackamon"



def main():
    global current_selection, splash

    update_menu_selection()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYDOWN and gameState == "Menu":
                if event.key == pygame.K_LEFT:
                    current_selection = (current_selection + 1) % len(menu_options)
                    update_menu_selection()

                if event.key == pygame.K_RIGHT:
                    current_selection = (current_selection - 1) % len(menu_options)
                    update_menu_selection()

                if event.key == pygame.K_UP:
                    handle_selection()

if __name__ == "__main__":
    update_menu_selection()  
    main()

