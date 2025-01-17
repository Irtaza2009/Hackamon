import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
import pygame
import time
import math
import random

pygame.init()

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

font = bitmap_font.load_font("PixelifySans-Regular.bdf")

desk_background = displayio.OnDiskBitmap("Desk-BG.bmp")
desk_bg_sprite = displayio.TileGrid(desk_background, pixel_shader=desk_background.pixel_shader)
station_background = displayio.OnDiskBitmap("Station-BG.bmp")
station_bg_sprite = displayio.TileGrid(station_background, pixel_shader=station_background.pixel_shader)
breakout_background = displayio.OnDiskBitmap("Breakout-BG.bmp")
breakout_bg_sprite = displayio.TileGrid(breakout_background, pixel_shader=breakout_background.pixel_shader)
splash.append(desk_bg_sprite)

tile_width = 32
tile_height = 32

brick_height = 8
brick_width = 16

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

button_1_sheet = displayio.OnDiskBitmap("Button-1-Spritesheet.bmp")

button_1_sprite = displayio.TileGrid(button_1_sheet,
                                    pixel_shader=button_1_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 3,
                                    y=display.height - tile_height - 30)

button_2_sheet = displayio.OnDiskBitmap("Button-2-Spritesheet.bmp")

button_2_sprite = displayio.TileGrid(button_2_sheet,
                                    pixel_shader=button_2_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 2 + 10,
                                    y=display.height - tile_height - 30)

button_3_sheet = displayio.OnDiskBitmap("Button-3-Spritesheet.bmp")

button_3_sprite = displayio.TileGrid(button_3_sheet,
                                    pixel_shader=button_3_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 2 + 40,
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

splash.append(button_1_sprite)

splash.append(button_2_sprite)

splash.append(button_3_sprite)

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


pointer_sheet = displayio.OnDiskBitmap("Pointer-Spritesheet-2x.bmp")
pointer_sprite_1 = displayio.TileGrid(pointer_sheet,
                                        width=1,
                                        pixel_shader=pointer_sheet.pixel_shader,
                                        height=1,
                                        tile_width=14,
                                        tile_height=12,
                                        default_tile=0,
                                        x=button_1_sprite.x + 16 // 2 - 14 // 2,
                                        y=button_1_sprite.y - 9)
pointer_sprite_2 = displayio.TileGrid(pointer_sheet,
                                        width=1,
                                        pixel_shader=pointer_sheet.pixel_shader,
                                        height=1,
                                        tile_width=14,
                                        tile_height=12,
                                        default_tile=0,
                                        x=button_2_sprite.x + 16 // 2 - 14 // 2,
                                        y=button_2_sprite.y - 9)
pointer_sprite_3 = displayio.TileGrid(pointer_sheet,
                                        width=1,
                                        pixel_shader=pointer_sheet.pixel_shader,
                                        height=1,
                                        tile_width=14,
                                        tile_height=12,
                                        default_tile=0,
                                        x=button_3_sprite.x + 16 // 2 - 14 // 2,
                                        y=button_3_sprite.y - 9)

splash.append(pointer_sprite_1)
splash.append(pointer_sprite_2)
splash.append(pointer_sprite_3)

                                


brick_sheet = displayio.OnDiskBitmap("Breakout-Bricks-Spritesheet.bmp")
ball_sheet = displayio.OnDiskBitmap("Breakout-Ball.bmp")

splash.append(hackamon_sprite_idle)

frame = 0
framePointer = 0
speed = 4
game_over = False
isJumping = False
facing_left = True
gameState = "Main"
happiness = 5000
battery = 5000
charging = False
chargingSprite = False
ball_delta_x = 1
ball_delta_y = 1
MAX_SPEED = 3  # Maximum ball speed
RANDOM_RANGE = 1  # Random range for offsetting ball direction



happiness_label = label.Label(
    font,
    text=str(happiness),
    color=0x000000,  # Black color
    anchor_point=(0.5, 0),
    anchored_position=(happiness_bar_sprite.x + 28, happiness_bar_sprite.y + 2)
)

splash.append(happiness_label)

battery_label = label.Label(
    font,
    text=str(battery),
    color=0x000000,  # Black color
    anchor_point=(0.5, 0),
    anchored_position=(battery_bar_sprite.x + 28, battery_bar_sprite.y + 2)
)

splash.append(battery_label)



def run_jump_animation():
   global frame, isJumping

   

   for jump_frame in range(hackamon_sheet_jump.width // tile_width):

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
    # Using the dimensions of the button and sprite for accurate detection (todo: create variables for these)
    if check_collision(
        hackamon_sprite_idle, button_1_sprite,
        tile_width, tile_height, 16, 18
    ) and gameState == "Main":
        button_1_sprite[0] = 1  
        print("Button Pressed!")
        time.sleep(0.5)
        gameState = "Station"
        to_charging_station()
    elif check_collision(
        hackamon_sprite_idle, button_2_sprite,
        tile_width, tile_height, 16, 18
    ) and gameState == "Main":
        button_2_sprite[0] = 1
    elif check_collision(
        hackamon_sprite_idle, button_2_sprite,
        tile_width, tile_height, 16, 18
    ) and (gameState == "Station" or gameState == "Breakout"):
        button_2_sprite[0] = 1
        print("Button Pressed!")
        time.sleep(0.5)
        to_main(gameState)
    elif check_collision(
        hackamon_sprite_idle, button_3_sprite,
        tile_width, tile_height, 16, 18
    ) and gameState == "Main":
        button_3_sprite[0] = 1
        print("Button Pressed!")
        time.sleep(0.5)
        gameState = "Breakout"
        to_breakout()

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
        hackamon_sprite_jump.x = 85
        hackamon_sprite_jump.y = 70
        charging = True
        chargingSprite = True


# Bricks for breakout

brick_sprites = []
rows = 4
columns = 6

for row in range(rows):
    for column in range(columns):
        brick_sprite = displayio.TileGrid(brick_sheet,
                                    pixel_shader=brick_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=brick_width,
                                    tile_height=brick_height,
                                    default_tile=0,
                                    x=column * brick_width + 11 + column * 2,
                                    y=row * brick_height + 9 + row * 2)
        brick_sprite[0] = column
        brick_sprites.append(brick_sprite)

# Ball for breakout

ball_sprite = displayio.TileGrid(ball_sheet,
                                pixel_shader=ball_sheet.pixel_shader,
                                width=1,
                                height=1,
                                tile_width=6,
                                tile_height=6,
                                default_tile=0,
                                x=(display.width - 6) // 2,
                                y=display.height // 2)

def manage_stats():
    global happiness, battery, game_over, charging, happiness_label, battery_label
    
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

    if gameState != "Breakout":
        splash.remove(happiness_label)
        splash.remove(battery_label)

        happiness_label = label.Label(
            font,
            text=str(happiness),
            color=0x000000,  # Black color
            anchor_point=(0.5, 0),
            anchored_position=(happiness_bar_sprite.x + 28, happiness_bar_sprite.y + 2)
        )
        splash.append(happiness_label)

        battery_label = label.Label(
        font,
        text=str(battery),
        color=0x000000,  # Black color
        anchor_point=(0.5, 0),
        anchored_position=(battery_bar_sprite.x + 28, battery_bar_sprite.y + 2)
        )

        splash.append(battery_label)
        
def breakout():
    global ball_sprite, game_over, ball_delta_x, ball_delta_y, MAX_SPEED, RANDOM_RANGE, happiness
    ball_sprite.y += round(ball_delta_y)
    ball_sprite.x += round(ball_delta_x)

    # Let's not make it impossible so capping the speed

    ball_delta_x = max(min(ball_delta_x * 1.01, MAX_SPEED), -MAX_SPEED)
    ball_delta_y = max(min(ball_delta_y * 1.01, MAX_SPEED), -MAX_SPEED)

    if ball_sprite.y > 128 - 10 - 6:
        ball_sprite.y = hackamon_sprite_idle.y 
        ball_sprite.x = hackamon_sprite_idle.x + 16

    if ball_sprite.y <= 0 + 7:
        ball_delta_y = -ball_delta_y  

    if ball_sprite.x >= 128 - 6 - 6:
        ball_delta_x = -ball_delta_x

    if ball_sprite.x <= 0 + 6:   
        ball_delta_x = -ball_delta_x

    if check_collision(
        ball_sprite, hackamon_sprite_idle,
        6, 6, tile_width, tile_height
    ):
        print("Ball Hit Hackamon!")
        ball_delta_y = -ball_delta_y 
        ball_delta_x = -ball_delta_x + random.randint(-RANDOM_RANGE, RANDOM_RANGE)

    for brick in brick_sprites:
        if check_collision(
            ball_sprite, brick,
            6, 6, brick_width, brick_height
        ):
            print("Ball Hit Brick!")
            brick_sprites.remove(brick)
            splash.remove(brick)
            ball_delta_y = -ball_delta_y + random.randint(-RANDOM_RANGE, RANDOM_RANGE)
            ball_delta_x = -ball_delta_x 
            happiness += 40

    # Ensuring ball direction remains within bounds after adding random direction offset
    ball_delta_x = max(min(ball_delta_x, MAX_SPEED), -MAX_SPEED)
    ball_delta_y = max(min(ball_delta_y, MAX_SPEED), -MAX_SPEED)

    if len(brick_sprites) == 0:
        print("Game Won!")
        if happiness < 4000:
            happiness += 1000
        else:
            happiness = 4999
        to_main(gameState)


                            
    

# Functions to switch between game states
def to_breakout():
    global gameState
    gameState = "Breakout"
    # remove all from splash
    splash.remove(hackamon_sprite_idle)
    splash.remove(desk_bg_sprite)
    splash.remove(button_1_sprite)
    splash.remove(button_2_sprite)
    splash.remove(button_3_sprite)
    splash.remove(happiness_bar_sprite)
    splash.remove(battery_bar_sprite)
    splash.remove(pointer_sprite_1)
    splash.remove(pointer_sprite_2)
    splash.remove(pointer_sprite_3)
    
    # add breakout background and sprites
    splash.append(breakout_bg_sprite)
    splash.append(button_2_sprite)
    for brick in brick_sprites:
        splash.append(brick)
    splash.append(pointer_sprite_1)
    splash.append(hackamon_sprite_idle)
    splash.append(ball_sprite)


    

    button_2_sprite.x = 16 + 10
    button_2_sprite.y = 128 - 18 - 10
    button_2_sprite[0] = 0

    pointer_sprite_1.x = button_2_sprite.x + 16 // 2 - 14 // 2
    pointer_sprite_1.y = button_2_sprite.y - 9

    hackamon_sprite_idle.x = display.width // 2 - tile_width // 2
    hackamon_sprite_idle.y = 118 - tile_height
    hackamon_sprite_jump.x = display.width // 2 - tile_width // 2
    hackamon_sprite_jump.y = 118 - tile_height




def to_charging_station():
    global gameState
    gameState = "Station"
    # remove all from splash
    splash.remove(hackamon_sprite_idle)
    splash.remove(button_1_sprite)
    splash.remove(button_2_sprite)
    splash.remove(button_3_sprite)
    splash.remove(happiness_bar_sprite)
    splash.remove(battery_bar_sprite)
    splash.remove(desk_bg_sprite)
    splash.remove(pointer_sprite_1)
    splash.remove(pointer_sprite_2)
    splash.remove(pointer_sprite_3)
    # add station background and sprites back
    splash.append(station_bg_sprite)
    splash.append(charging_station_sprite)
    splash.append(happiness_bar_sprite)
    splash.append(battery_bar_sprite)
    splash.append(button_2_sprite)

    button_2_sprite.x = 16 + 10
    button_2_sprite.y = 128 - 18 - 10
    button_2_sprite[0] = 0

    splash.append(pointer_sprite_1)
    splash.append(pointer_sprite_2)

    splash.append(hackamon_sprite_idle)

    pointer_sprite_1.x = button_2_sprite.x + 16 // 2 - 14 // 2
    pointer_sprite_1.y = button_2_sprite.y - 9

    pointer_sprite_2.x = charging_station_sprite.x + 55 // 2 - 14 // 2
    pointer_sprite_2.y = charging_station_sprite.y + 42 // 2 - 18 // 2

    hackamon_sprite_idle.x = 10
    hackamon_sprite_idle.y = 128 - tile_height - 10
    hackamon_sprite_jump.x = 10
    hackamon_sprite_jump.y = 128 - tile_height - 10

def to_main(prevGameState):
    global gameState
    gameState = "Main"
    # remove all from splash

    # if from breakout
    if prevGameState == "Breakout":
        splash.remove(breakout_bg_sprite)
        for brick in brick_sprites:
            splash.remove(brick)
        splash.remove(ball_sprite)
        splash.remove(pointer_sprite_1)
        
    splash.remove(hackamon_sprite_idle)

    # if from station
    if prevGameState == "Station": 
        splash.remove(charging_station_sprite)
        splash.remove(station_bg_sprite)
        splash.remove(happiness_bar_sprite)
        splash.remove(battery_bar_sprite)
        splash.remove(pointer_sprite_1)
        splash.remove(pointer_sprite_2)
    splash.remove(button_2_sprite)
    # add main background and sprites back
    splash.append(desk_bg_sprite)
    splash.append(button_1_sprite)
    splash.append(button_2_sprite)
    splash.append(button_3_sprite)
    splash.append(happiness_bar_sprite)
    splash.append(battery_bar_sprite)
   

    button_2_sprite.x = (display.width - tile_width) // 2 + 10
    button_2_sprite.y = display.height - tile_height - 30

    button_1_sprite[0] = 0
    button_2_sprite[0] = 0
    button_3_sprite[0] = 0

    splash.append(pointer_sprite_1)
    splash.append(pointer_sprite_2)
    splash.append(pointer_sprite_3)

    pointer_sprite_1.x=button_1_sprite.x + 16 // 2 - 14 // 2
    pointer_sprite_1.y=button_1_sprite.y - 9
    pointer_sprite_2.x=button_2_sprite.x + 16 // 2 - 14 // 2
    pointer_sprite_2.y=button_2_sprite.y - 9
    pointer_sprite_3.x=button_3_sprite.x + 16 // 2 - 14 // 2
    pointer_sprite_3.y=button_3_sprite.y - 9


    splash.append(hackamon_sprite_idle)

    hackamon_sprite_idle.x = (display.width - tile_width) // 2
    hackamon_sprite_idle.y = display.height - tile_height - 40
    hackamon_sprite_jump.x = (display.width - tile_width) // 2
    hackamon_sprite_jump.y = display.height - tile_height - 40


        
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
            if (gameState == "Main" and hackamon_sprite_idle.x > 24) or (gameState == "Station" and hackamon_sprite_idle.x > 0) or (gameState == "Breakout" and hackamon_sprite_idle.x > 0):
                facing_left = True
                hackamon_sprite_idle.x -= speed
                hackamon_sprite_jump.x -= speed
                hackamon_sprite_idle.flip_x = False
                hackamon_sprite_jump.flip_x = False

        if keys[pygame.K_RIGHT]:
            charging = False
            if (gameState == "Main" and hackamon_sprite_idle.x < 78) or (gameState == "Station" and hackamon_sprite_idle.x < 128 - tile_width) or (gameState == "Breakout" and hackamon_sprite_idle.x < 128 - tile_width):
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
        
        if keys[pygame.K_SPACE] and not isJumping and not charging:
            isJumping = True
            splash.remove(hackamon_sprite_idle)
            splash.append(hackamon_sprite_jump)
            run_jump_animation()
            check_button_press()
            if gameState == "Station":
                 charging_station()

        
        
        if chargingSprite == True and not charging:
            chargingSprite = False
            splash.remove(hackamon_sprite_charging)
            hackamon_sprite_idle.x = 128 - tile_width - 10
            hackamon_sprite_idle.y = 128 - tile_height - 10
            hackamon_sprite_jump.x = 128 - tile_width - 10
            hackamon_sprite_jump.y = 128 - tile_height - 10

        if gameState == "Breakout":
            breakout()

        manage_stats()

        


    
    pointer_sprite_1[0] = framePointer 
    pointer_sprite_2[0] = framePointer
    pointer_sprite_3[0] = framePointer
    framePointer = (framePointer + 1) % (pointer_sheet.width // 14)


    if charging:
        hackamon_sprite_charging[0] = frame 

    hackamon_sprite_idle[0] = frame
    frame = (frame + 1) % (hackamon_sheet_idle.width // tile_width)

    time.sleep(0.1)
