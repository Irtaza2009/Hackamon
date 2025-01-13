import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame
import time
import math

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

desk_background = displayio.OnDiskBitmap("Desk-BG.bmp")
desk_bg_sprite = displayio.TileGrid(desk_background, pixel_shader=desk_background.pixel_shader)
station_background = displayio.OnDiskBitmap("Station-BG.bmp")
station_bg_sprite = displayio.TileGrid(station_background, pixel_shader=station_background.pixel_shader)
splash.append(desk_bg_sprite)

tile_width = 32
tile_height = 32

hackamon_sheet_idle = displayio.OnDiskBitmap("Hackamon-1-Idle-Spritesheet.bmp")
hackamon_sprite_idle = displayio.TileGrid(hackamon_sheet_idle,
                                     pixel_shader=hackamon_sheet_idle.pixel_shader,
                                     width=1,
                                     height=1,
                                     tile_width=tile_width,
                                     tile_height=tile_height,
                                     default_tile=0,
                                     x=(display.width - tile_width) // 2,
                                     y=display.height - tile_height - 40)


hackamon_sheet_jump = displayio.OnDiskBitmap("Hackamon-1-Jump-Spritesheet.bmp")
hackamon_sprite_jump = displayio.TileGrid(hackamon_sheet_jump,
                                        pixel_shader=hackamon_sheet_jump.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=tile_width,
                                        tile_height=tile_height,
                                        default_tile=0,
                                        x=(display.width - tile_width) // 2,
                                        y=display.height - tile_height - 40)

hackamon_sheet_charging = displayio.OnDiskBitmap("Hackamon-1-Charging-Spritesheet.bmp")
hackamon_sprite_charging = displayio.TileGrid(hackamon_sheet_charging,
                                        pixel_shader=hackamon_sheet_charging.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=tile_width,
                                        tile_height=tile_height,
                                        default_tile=0,
                                        x=85,
                                        y=70)

button_sheet = displayio.OnDiskBitmap("Button-1-Spritesheet.bmp")

button_sprite = displayio.TileGrid(button_sheet,
                                    pixel_shader=button_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 3,
                                    y=display.height - tile_height - 30)

happiness_bar_sheet = displayio.OnDiskBitmap("Happiness-Bar-Spritesheet.bmp")

happiness_bar_sprite = displayio.TileGrid(happiness_bar_sheet,
                                    pixel_shader=happiness_bar_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=48,
                                    tile_height=10,
                                    default_tile=0,
                                    x=5,
                                    y=8)

splash.append(happiness_bar_sprite)

battery_bar_sheet = displayio.OnDiskBitmap("Battery-Bar-Spritesheet.bmp")

battery_bar_sprite = displayio.TileGrid(battery_bar_sheet,
                                    pixel_shader=battery_bar_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=48,
                                    tile_height=10,
                                    default_tile=0,
                                    x=5,
                                    y=20)

splash.append(battery_bar_sprite)

splash.append(button_sprite)

splash.append(hackamon_sprite_idle)

charging_station_sheet = displayio.OnDiskBitmap("Charging-Station.bmp")
charging_station_sprite = displayio.TileGrid(charging_station_sheet,
                                    pixel_shader=charging_station_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=55,
                                    tile_height=42,
                                    default_tile=0,
                                    x=72,
                                    y=70)

frame = 0
speed = 4
game_over = False
isJumping = False
facing_left = True
gameState = "Main"
happiness = 5000
battery = 5000
charging = False
chargingSprite = False


def run_jump_animation():
   global frame, isJumping

   

   for jump_frame in range(hackamon_sheet_jump.width // tile_width):

    """ if jump_frame == 0:
            hackamon_sprite_jump.y -= 10
       elif jump_frame == hackamon_sheet_jump.width // tile_width - 1:
            hackamon_sprite_jump.y += 10 """

    hackamon_sprite_jump[0] = jump_frame
    time.sleep(0.1)

   

   splash.remove(hackamon_sprite_jump)
   splash.append(hackamon_sprite_idle)
   isJumping = False

# Collision function
def check_collision(sprite1, sprite2, width1, height1, width2, height2):
    return (
        sprite1.x < sprite2.x + width2 and
        sprite1.x + width1 > sprite2.x and
        sprite1.y < sprite2.y + height2 and
        sprite1.y + height1 > sprite2.y
    )

def check_button_press():
    global gameState
    print("Checking Button Press...")
    # Use the dimensions of the button and sprite for accurate detection
    if check_collision(
        hackamon_sprite_idle, button_sprite,
        tile_width, tile_height, 16, 18
    ):
        button_sprite[0] = 1  # Switch button to pressed state
        print("Button Pressed!")
        time.sleep(0.5)
        gameState = "Station"
        to_mini_game()

def charging_station():
    global battery, facing_left, charging, chargingSprite
    if check_collision(
        hackamon_sprite_idle, charging_station_sprite,
        tile_width, tile_height, 55, 42
    ):
        print("Charging!")
        if facing_left == False:
            facing_left = True
            hackamon_sprite_idle.flip_x = False
            hackamon_sprite_jump.flip_x = False

        splash.append(hackamon_sprite_charging)


        hackamon_sprite_idle.x = 85
        hackamon_sprite_idle.y = 70
        charging = True
        chargingSprite = True

def manage_stats():
    global happiness, battery, game_over, charging
    if happiness <= 0 or battery <= 0:
        print("Game Over!")
        game_over = True
    else:
        happiness -= 1
        print("Happiness: " + str(happiness))
        happiness_bar_sprite[0] = 4 - math.ceil(happiness // 1000)
        if charging:
            if battery < 4999:
                battery += 1
            elif battery == 4999:
                charging = False
        else:
            battery -= 1
        print("Battery: " + str(battery))
        battery_bar_sprite[0] = 4 - math.ceil(battery // 1000)
        
def to_mini_game():
    global gameState
    # remove all from splash
    splash.remove(hackamon_sprite_idle)
    splash.remove(button_sprite)
    splash.remove(happiness_bar_sprite)
    splash.remove(battery_bar_sprite)
    # add station background and sprites back
    splash.append(station_bg_sprite)
    splash.append(charging_station_sprite)
    splash.append(hackamon_sprite_idle)
    splash.append(happiness_bar_sprite)
    splash.append(battery_bar_sprite)


    
    



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
            charging = False
            if (gameState == "Main" and hackamon_sprite_idle.x > 24) or (gameState == "Station" and hackamon_sprite_idle.x > 0):
                facing_left = True
                hackamon_sprite_idle.x -= speed
                hackamon_sprite_jump.x -= speed
                hackamon_sprite_idle.flip_x = False
                hackamon_sprite_jump.flip_x = False

        if keys[pygame.K_RIGHT]:
            charging = False
            if (gameState == "Main" and hackamon_sprite_idle.x < 78) or (gameState == "Station" and hackamon_sprite_idle.x < 128 - tile_width):
                facing_left = False
                hackamon_sprite_idle.x += speed
                hackamon_sprite_jump.x += speed
                hackamon_sprite_idle.flip_x = True
                hackamon_sprite_jump.flip_x = True

        # For testing! I know there will be only 3 buttons :)
        if keys[pygame.K_UP]:
            charging = False
            if (gameState == "Main" and hackamon_sprite_idle.y > 64 - 20) or (gameState == "Station" and hackamon_sprite_idle.y > 96 - 20):
                hackamon_sprite_idle.y -= speed
                hackamon_sprite_jump.y -= speed
                
        if keys[pygame.K_DOWN]:
            charging = False
            if (gameState == "Main" and hackamon_sprite_idle.y < 92 - tile_height) or (gameState == "Station" and hackamon_sprite_idle.y < 128 - tile_height):
                hackamon_sprite_idle.y += speed
                hackamon_sprite_jump.y += speed
        
        if keys[pygame.K_SPACE] and not isJumping:
            isJumping = True
            charging = False
            splash.remove(hackamon_sprite_idle)
            splash.append(hackamon_sprite_jump)
            run_jump_animation()
            check_button_press()
            charging_station()

        
        
        if chargingSprite == True and not charging:
            chargingSprite = False
            splash.remove(hackamon_sprite_charging)

        manage_stats()





    if charging:
        hackamon_sprite_charging[0] = frame 

    hackamon_sprite_idle[0] = frame
    frame = (frame + 1) % (hackamon_sheet_idle.width // tile_width)

    time.sleep(0.1)
