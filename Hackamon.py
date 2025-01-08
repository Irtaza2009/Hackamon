import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

desk_background = displayio.OnDiskBitmap("Desk-BG.bmp")
bg_sprite = displayio.TileGrid(desk_background, pixel_shader=desk_background.pixel_shader)
splash.append(bg_sprite)

tile_width = 32
tile_height = 32

hackamon_sheet = displayio.OnDiskBitmap("Hackamon-1-Idle-Spritesheet.bmp")

hackamon_sprite = displayio.TileGrid(hackamon_sheet,
                                     pixel_shader=hackamon_sheet.pixel_shader,
                                     width=1,
                                     height=1,
                                     tile_width=tile_width,
                                     tile_height=tile_height,
                                     default_tile=0,
                                     x=(display.width - tile_width) // 2,
                                     y=display.height - tile_height - 40)

splash.append(hackamon_sprite)

frame = 0
speed = 4
game_over = False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if display.check_quit():
        break



    keys = pygame.key.get_pressed()

    if game_over == False:
        if keys[pygame.K_LEFT]:
            if hackamon_sprite.x > 24:
                hackamon_sprite.x -= speed
        if keys[pygame.K_RIGHT]:
            if hackamon_sprite.x < 78:
                hackamon_sprite.x += speed

        # For testing! I know there will be only 3 buttons :)
        if keys[pygame.K_UP]:
            if hackamon_sprite.y > 64 - 20:
                hackamon_sprite.y -= speed
        if keys[pygame.K_DOWN]:
            if hackamon_sprite.y < 92 - tile_height:
                hackamon_sprite.y += speed






    hackamon_sprite[0] = frame
    frame = (frame + 1) % (hackamon_sheet.width // tile_width)

    time.sleep(0.1)
