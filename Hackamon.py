import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
import pygame
import asyncio
import time
import math
import random

pygame.init()



# test leaderboard data
leaderboard_data = [
    {"username": "Irtaza", "pet_level": 6},
    {"username": "Test", "pet_level": 4},
    {"username": "Pet", "pet_level": 3},
    {"username": "Childe", "pet_level": 2},
    {"username": "Robo", "pet_level": 1}
]

menu_options = [
    {"text": "Stopwatch", "unselected_tile": 0, "selected_tile": 4},
    {"text": "Dice Roll", "unselected_tile": 1, "selected_tile": 5},
    {"text": "Coin Flip", "unselected_tile": 2, "selected_tile": 6},
    {"text": "Hackamon", "unselected_tile": 3, "selected_tile": 7},
]

display = PyGameDisplay(width=128, height=128)
splash = displayio.Group()
display.show(splash)

font = bitmap_font.load_font("fonts/PixelifySans-Regular.bdf")
#font8px = bitmap_font.load_font("fonts/PixelifySans-Regular-8px.bdf")
#font24px = bitmap_font.load_font("fonts/PixelifySans-Regular-24px.bdf")
#font12px = bitmap_font.load_font("fonts/PixelifySans-Regular-12px.bdf")
font8px = bitmap_font.load_font("fonts/pixelade-8px.bdf")
font24px = bitmap_font.load_font("fonts/pixelade-24px.bdf")
font12px = bitmap_font.load_font("fonts/pixelade-12px.bdf")


desk_background = displayio.OnDiskBitmap("assets/Desk-BG.bmp")
desk_bg_sprite = displayio.TileGrid(desk_background, pixel_shader=desk_background.pixel_shader)
station_background = displayio.OnDiskBitmap("assets/Station-BG.bmp")
station_bg_sprite = displayio.TileGrid(station_background, pixel_shader=station_background.pixel_shader)
breakout_background = displayio.OnDiskBitmap("assets/Breakout-BG.bmp")
breakout_bg_sprite = displayio.TileGrid(breakout_background, pixel_shader=breakout_background.pixel_shader)
leaderboard_background = displayio.OnDiskBitmap("assets/Leaderboard-BG.bmp")
leaderboard_bg_sprite = displayio.TileGrid(leaderboard_background, pixel_shader=leaderboard_background.pixel_shader)
menu_bg_sheet = displayio.OnDiskBitmap("assets/Menu-BG.bmp")
menu_bg_sprite = displayio.TileGrid(menu_bg_sheet, pixel_shader=menu_bg_sheet.pixel_shader)
splash.append(menu_bg_sprite)

menu_box_sheet = displayio.OnDiskBitmap("assets/Menu-Box-Spritesheet.bmp")
menu_box_sprite = displayio.TileGrid(menu_box_sheet,
                                    pixel_shader=menu_box_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=100,
                                    tile_height=25,
                                    default_tile=0,
                                    x=14,
                                    y=5)

tile_width = 32
tile_height = 32

brick_height = 8
brick_width = 16

hackamon_sheet_idle = displayio.OnDiskBitmap("assets/Hackamon-1-Idle-Spritesheet.bmp")
hackamon_sprite_idle = displayio.TileGrid(hackamon_sheet_idle,
                                     pixel_shader=hackamon_sheet_idle.pixel_shader,
                                     width=1,
                                     height=1,
                                     tile_width=tile_width,
                                     tile_height=tile_height,
                                     default_tile=0,
                                     x=(display.width - tile_width) // 2,
                                     y=display.height - tile_height - 40)


hackamon_sheet_jump = displayio.OnDiskBitmap("assets/Hackamon-1-Jump-Spritesheet.bmp")
hackamon_sprite_jump = displayio.TileGrid(hackamon_sheet_jump,
                                        pixel_shader=hackamon_sheet_jump.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=tile_width,
                                        tile_height=tile_height,
                                        default_tile=0,
                                        x=(display.width - tile_width) // 2,
                                        y=display.height - tile_height - 40)

hackamon_sheet_charging = displayio.OnDiskBitmap("assets/Hackamon-1-Charging-Spritesheet.bmp")
hackamon_sprite_charging = displayio.TileGrid(hackamon_sheet_charging,
                                        pixel_shader=hackamon_sheet_charging.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=tile_width,
                                        tile_height=tile_height,
                                        default_tile=0,
                                        x=85,
                                        y=70)

button_1_sheet = displayio.OnDiskBitmap("assets/Button-1-Spritesheet.bmp")

button_1_sprite = displayio.TileGrid(button_1_sheet,
                                    pixel_shader=button_1_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 3,
                                    y=display.height - tile_height - 30)

button_2_sheet = displayio.OnDiskBitmap("assets/Button-2-Spritesheet.bmp")

button_2_sprite = displayio.TileGrid(button_2_sheet,
                                    pixel_shader=button_2_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 2 + 10,
                                    y=display.height - tile_height - 30)

button_3_sheet = displayio.OnDiskBitmap("assets/Button-3-Spritesheet.bmp")

button_3_sprite = displayio.TileGrid(button_3_sheet,
                                    pixel_shader=button_3_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=16,
                                    tile_height=18,
                                    default_tile=0,
                                    x=(display.width - tile_width) // 2 + 40,
                                    y=display.height - tile_height - 30)

back_button_sheet = displayio.OnDiskBitmap("assets/Back-Button-Spritesheet.bmp")
back_button_sprite = displayio.TileGrid(back_button_sheet,
                                    pixel_shader=back_button_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=14,
                                    tile_height=10,
                                    default_tile=0,
                                    x=10,
                                    y=10)

happiness_bar_sheet = displayio.OnDiskBitmap("assets/Happiness-Bar-Spritesheet.bmp")

happiness_bar_sprite = displayio.TileGrid(happiness_bar_sheet,
                                    pixel_shader=happiness_bar_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=48,
                                    tile_height=10,
                                    default_tile=0,
                                    x=5,
                                    y=8)

#splash.append(happiness_bar_sprite)



battery_bar_sheet = displayio.OnDiskBitmap("assets/Battery-Bar-Spritesheet.bmp")

battery_bar_sprite = displayio.TileGrid(battery_bar_sheet,
                                    pixel_shader=battery_bar_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=48,
                                    tile_height=10,
                                    default_tile=0,
                                    x=5,
                                    y=20)

#splash.append(battery_bar_sprite)

day_night_cycle_bar_sheet = displayio.OnDiskBitmap("assets/Day-Night-Bar-Spritesheet.bmp")
day_night_cycle_bar_sprite = displayio.TileGrid(day_night_cycle_bar_sheet,
                                    pixel_shader=day_night_cycle_bar_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=48,
                                    tile_height=10,
                                    default_tile=0,
                                    x=5,
                                    y=32)

#splash.append(day_night_cycle_bar_sprite)

#splash.append(button_1_sprite)

#splash.append(button_2_sprite)

#splash.append(button_3_sprite)

charging_station_sheet = displayio.OnDiskBitmap("assets/Charging-Station.bmp")
charging_station_sprite = displayio.TileGrid(charging_station_sheet,
                                    pixel_shader=charging_station_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=55,
                                    tile_height=42,
                                    default_tile=0,
                                    x=72,
                                    y=70)


pointer_sheet = displayio.OnDiskBitmap("assets/Pointer-Spritesheet-2x.bmp")
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

pointer_left_sheet = displayio.OnDiskBitmap("assets/Pointer-Left-Spritesheet-2x.bmp")
pointer_left_sprite = displayio.TileGrid(pointer_left_sheet,
                                        width=1,
                                        pixel_shader=pointer_sheet.pixel_shader,
                                        height=1,
                                        tile_width=14,
                                        tile_height=12,
                                        default_tile=0,
                                        x=10,
                                        y=10)

#splash.append(pointer_sprite_1)
#splash.append(pointer_sprite_2)
#splash.append(pointer_sprite_3)

player_card_sheet = displayio.OnDiskBitmap("assets/Player-Card-Spritesheet.bmp")
player_card_sprite = displayio.TileGrid(player_card_sheet,
                                    pixel_shader=player_card_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=100,
                                    tile_height=20,
                                    default_tile=0,
                                    x=14,
                                    y=5)

                                


brick_sheet = displayio.OnDiskBitmap("assets/Breakout-Bricks-Spritesheet.bmp")
ball_sheet = displayio.OnDiskBitmap("assets/Breakout-Ball.bmp")

dice_sheet = displayio.OnDiskBitmap("assets/Dice-Spritesheet.bmp")
dice_sprite = displayio.TileGrid(dice_sheet,
                                    pixel_shader=dice_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=42,
                                    tile_height=42,
                                    default_tile=0,
                                    x=43,
                                    y=43)

coin_sheet = displayio.OnDiskBitmap("assets/Coin-Spritesheet.bmp")
coin_sprite = displayio.TileGrid(coin_sheet,
                                    pixel_shader=coin_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=42,
                                    tile_height=42,
                                    default_tile=0,
                                    x=43,
                                    y=43)

#splash.append(hackamon_sprite_idle)

frame = 0
framePointer = 0
frameBackButton = 0
speed = 4
game_over = False
isJumping = False
facing_left = True
gameState = "Menu"
happiness = 5000
battery = 5000
day_night = 5000
day = 0
level = 0
rolling = False
flipping = False
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

#splash.append(happiness_label)

battery_label = label.Label(
    font,
    text=str(battery),
    color=0x000000,  # Black color
    anchor_point=(0.5, 0),
    anchored_position=(battery_bar_sprite.x + 28, battery_bar_sprite.y + 2)
)

#splash.append(battery_label)

level_label = label.Label(
    font24px,
    text="Level: " + str(level),
    color=0xFFFFFF,
    anchor_point=(0.5, 0.5),
    anchored_position=(display.width // 2, display.height // 2)
)


# menu
menu_box_sprites = []
menu_box_options = []
current_selection = 0

if gameState == "Menu":
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
            font12px, text=option["text"], color=0x7a8af0, anchor_point=(0, 0), anchored_position=(x + 5, y + 7)
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

update_menu_selection()

def handle_selection():
    global gameState
    if current_selection == 0:
        print("Time")
    elif current_selection == 1:
        print("Dice Roll")
        to_dice_roll()
        time.sleep(0.1)
    elif current_selection == 2:
        print("Coin Flip")
        to_coin_flip()
        time.sleep(0.1)
    elif current_selection == 3:
        print("Hackamon")
        to_main(gameState)
        time.sleep(0.1)

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
        to_leaderboard()
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
    global happiness, battery, game_over, charging, happiness_label, battery_label, level_label, day_night, day, level
    
    if happiness <= 0 or battery <= 0:
        print("Game Over!")
        to_main(gameState)
        game_over = True
    else:
        happiness -= 1
        #print("Happiness: " + str(happiness))
        happiness_bar_sprite[0] = 4 - math.ceil(happiness // 1000)
        if charging:
            if battery < 4999:
                battery += 1
            elif battery == 4999:
                charging = False
        else:
            battery -= 1
        #print("Battery: " + str(battery))
        battery_bar_sprite[0] = 4 - math.ceil(battery // 1000)

    if gameState != "Breakout" and gameState != "Leaderboard" and gameState != "Menu" and gameState != "Dice" and gameState != "Coin":
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

    
    if day_night == 0:
        day += 1
        day_night = 4900
        level += 1


        level_label = label.Label(
            font24px,
            text="Level: " + str(level),
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(display.width // 2, display.height // 2)
        )

        background_rect = Rect(2, 50, 126, 30, fill=0x222034)
    
        # Append the rectangle and the label to the splash group
        splash.append(background_rect)

        splash.append(level_label)
        time.sleep(2)
        splash.remove(level_label)
        splash.remove(background_rect)

    else:
        day_night -= 20

        day_night_cycle_bar_sprite[0] = 4 - math.ceil(day_night // 1000)

        
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


# player data in leaderboard


player_card_sprites = []
player_card_usernames = []
player_card_pet_levels = []

def create_player_card(username, pet_level, x, y):             
    player_card_sprite = displayio.TileGrid(player_card_sheet,
                                    pixel_shader=player_card_sheet.pixel_shader,
                                    width=1,
                                    height=1,
                                    tile_width=100,
                                    tile_height=20,
                                    default_tile=0,
                                    x=x,
                                    y=y)
    username_label = label.Label(font12px, text=username, color=0x7a8af0, anchor_point=(0, 0), anchored_position=(x + 5, y + 5))
    pet_level_label = label.Label(font12px, text="Lvl: " + str(pet_level), color=0x3f3f74, anchor_point=(0, 0), anchored_position=(x + 65, y + 5))
    
    
    player_card_sprite[0] = (y - 10) / 22

    player_card_sprites.append(player_card_sprite)
    player_card_usernames.append(username_label)
    player_card_pet_levels.append(pet_level_label)

    splash.append(player_card_sprite)
    splash.append(username_label)
    splash.append(pet_level_label)

# dice roll

def roll_dice():
    global rolling
    for _ in range(2):  
        for face in range(6):  
            dice_sprite[0] = face 
            time.sleep(0.1) 

    # Stopping at a random face
    random_face = random.randint(0, 5)  
    dice_sprite[0] = random_face  

    print("The dice landed on face: ", random_face + 1)  # Print the result
    time.sleep(0.1)
    rolling = False

# coin flip

def flip_coin():
    global flipping
    for _ in range(2):  
        for face in range(8):  
            coin_sprite[0] = face 
            time.sleep(0.1)
    # Stop at head or tails
    random_face = 0 if random.randint(0, 1) == 0 else 4
    coin_sprite[0] = random_face

    print("The coin landed on: ", 'Heads' if random_face == 0 else 'Tails')  # Print the result
    time.sleep(0.1)
    flipping = False
    

# Functions to switch between game states

def to_leaderboard():
    global gameState
    gameState = "Leaderboard"
    # remove all from splash
    splash.remove(hackamon_sprite_idle)
    splash.remove(desk_bg_sprite)
    splash.remove(button_1_sprite)
    splash.remove(button_2_sprite)
    splash.remove(button_3_sprite)
    splash.remove(happiness_bar_sprite)
    splash.remove(battery_bar_sprite)
    splash.remove(day_night_cycle_bar_sprite)
    splash.remove(pointer_sprite_1)
    splash.remove(pointer_sprite_2)
    splash.remove(pointer_sprite_3)

    # leaderboard background and sprites
    splash.append(leaderboard_bg_sprite)
    # player cards for the leaderboard
    y_position = 10
    for player in leaderboard_data:
        create_player_card(player['username'], player['pet_level'], 14, y_position)
        y_position += 20 + 2
    #splash.append(back_button_sprite)
    splash.append(pointer_sprite_1)
    splash.append(pointer_sprite_2)
    splash.append(pointer_left_sprite)

    pointer_sprite_1.x = 24 - 14 // 2
    pointer_sprite_1.y = 128 - 10
    pointer_sprite_2.x = 128 - 24 - 14 // 2
    pointer_sprite_2.y = 128 - 10
    pointer_sprite_2.flip_y = True
    pointer_left_sprite.x = 128 // 2 - 14 // 2
    pointer_left_sprite.y = 128 - 10

    #back_button_sprite.x = 128 // 2 - 14 // 2
    #back_button_sprite.y = 128 - 10 



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
    splash.remove(day_night_cycle_bar_sprite)
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
    splash.remove(day_night_cycle_bar_sprite)
    splash.remove(desk_bg_sprite)
    splash.remove(pointer_sprite_1)
    splash.remove(pointer_sprite_2)
    splash.remove(pointer_sprite_3)
    # add station background and sprites back
    splash.append(station_bg_sprite)
    splash.append(charging_station_sprite)
    splash.append(happiness_bar_sprite)
    splash.append(day_night_cycle_bar_sprite)
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

    if prevGameState == "Leaderboard":
        splash.remove(leaderboard_bg_sprite)
        for player_card in player_card_sprites:
            player_card_sprites.remove(player_card)
            splash.remove(player_card)
        for username in player_card_usernames:
            player_card_usernames.remove(username)
            splash.remove(username)
        for pet_level in player_card_pet_levels:
            player_card_pet_levels.remove(pet_level)
            splash.remove(pet_level)
        #splash.remove(back_button_sprite)
        splash.remove(pointer_sprite_1)
        pointer_sprite_2.flip_y = False
        splash.remove(pointer_sprite_2)
        splash.remove(pointer_left_sprite)

    elif prevGameState == "Menu":
        for menu_box_sprite in menu_box_sprites:
            menu_box_sprites.remove(menu_box_sprite)
            splash.remove(menu_box_sprite)
        for option_label in menu_box_options:
            menu_box_options.remove(option_label)
            splash.remove(option_label)
        splash.remove(menu_bg_sprite)
        splash.append(happiness_label)
        splash.append(battery_label)
        
    else:


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
            splash.remove(day_night_cycle_bar_sprite)
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
    splash.append(day_night_cycle_bar_sprite)
   

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

def to_dice_roll():
    global gameState, dice_roll_label, dice_title_label
    gameState = "Dice"

    for menu_box_sprite in menu_box_sprites:
        menu_box_sprites.remove(menu_box_sprite)
        splash.remove(menu_box_sprite)
    for option_label in menu_box_options:
        menu_box_options.remove(option_label)
        splash.remove(option_label)
    splash.remove(menu_bg_sprite)

    splash.append(menu_bg_sprite)
    splash.append(dice_sprite)
    splash.append(pointer_sprite_3)
    dice_title_label = label.Label(font24px,
            text="Dice-Roll",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(display.width // 2, display.height // 6)
        )
    splash.append(dice_title_label)
    dice_roll_label = label.Label(font12px,
            text="Roll the dice!",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(display.width // 2, display.height - display.height // 4.5)
        )
    splash.append(dice_roll_label)
    pointer_sprite_3.x = 128 // 2 - 16 // 2
    pointer_sprite_3.y = 128 - 128 // 7

def to_coin_flip():
    global gameState, coin_flip_label, coin_title_label
    gameState = "Coin"

    for menu_box_sprite in menu_box_sprites:
        menu_box_sprites.remove(menu_box_sprite)
        splash.remove(menu_box_sprite)
    for option_label in menu_box_options:
        menu_box_options.remove(option_label)
        splash.remove(option_label)
    splash.remove(menu_bg_sprite)

    splash.append(menu_bg_sprite)
    splash.append(coin_sprite)
    splash.append(pointer_sprite_3)
    coin_title_label = label.Label(font24px,
            text="Coin-Flip",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(display.width // 2, display.height // 6)
        )
    splash.append(coin_title_label)
    coin_flip_label = label.Label(font12px,
            text="Flip the coin!",
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(display.width // 2, display.height - display.height // 4.5)
        )
    splash.append(coin_flip_label)
    pointer_sprite_3.x = 128 // 2 - 16 // 2
    pointer_sprite_3.y = 128 - 128 // 7

def to_menu(prevGameState):
    global gameState, dice_roll_label, dice_title_label, menu_box_sprites, menu_box_options, coin_flip_label, coin_title_label

    gameState = "Menu"

    # remove all from splash
    if prevGameState == "Main":
        splash.remove(hackamon_sprite_idle)
        splash.remove(desk_bg_sprite)
        splash.remove(button_1_sprite)
        splash.remove(button_2_sprite)
        splash.remove(button_3_sprite)
        splash.remove(happiness_bar_sprite)
        splash.remove(battery_bar_sprite)
        splash.remove(day_night_cycle_bar_sprite)
        splash.remove(pointer_sprite_1)
        splash.remove(pointer_sprite_2)
        splash.remove(pointer_sprite_3)
    
    if prevGameState == "Dice":
        splash.remove(menu_bg_sprite)
        splash.remove(dice_sprite)
        splash.remove(pointer_sprite_3)
        splash.remove(dice_roll_label)
        splash.remove(dice_title_label)

    if prevGameState == "Coin":
        splash.remove(menu_bg_sprite)
        splash.remove(coin_sprite)
        splash.remove(pointer_sprite_3)
        splash.remove(coin_flip_label)
        splash.remove(coin_title_label)

    
    
    # add to splash

    splash.append(menu_bg_sprite)

    menu_box_sprites = []
    menu_box_options = []

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
            font12px, text=option["text"], color=0x7a8af0, anchor_point=(0, 0), anchored_position=(x + 5, y + 7)
        )

        menu_box_sprites.append(menu_box_sprite)
        menu_box_options.append(option_label)


        splash.append(menu_box_sprite)
        splash.append(option_label)


    update_menu_selection()




async def main():
    global frame, framePointer, frameBackButton, isJumping, facing_left, gameState, charging, chargingSprite, current_selection, rolling, flipping
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

                if event.key == pygame.K_SPACE:
                    handle_selection()

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
                if gameState == "Dice" or gameState == "Coin":
                    to_menu(gameState)

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
            
            if keys[pygame.K_SPACE] and gameState == "Leaderboard":
                    time.sleep(0.5)
                    to_main(gameState)
            elif keys[pygame.K_SPACE] and not isJumping and not charging and gameState != "Menu" and gameState != "Dice" and gameState != "Coin":        
                isJumping = True
                splash.remove(hackamon_sprite_idle)
                splash.append(hackamon_sprite_jump)
                run_jump_animation()
                check_button_press()
                if gameState == "Station":
                    charging_station()
            elif keys[pygame.K_SPACE] and gameState == "Dice" and not rolling:
                rolling = True
                roll_dice()
            elif keys[pygame.K_SPACE] and gameState == "Coin" and not flipping:
                flipping = True
                flip_coin()

            
            
            if chargingSprite == True and not charging:
                chargingSprite = False
                splash.remove(hackamon_sprite_charging)
                hackamon_sprite_idle.x = 128 - tile_width - 10
                hackamon_sprite_idle.y = 128 - tile_height - 10
                hackamon_sprite_jump.x = 128 - tile_width - 10
                hackamon_sprite_jump.y = 128 - tile_height - 10

            if gameState == "Breakout":
                breakout()
            
            if gameState != "Menu" and gameState != "Dice" and gameState != "Coin":
                manage_stats()

            


        
        pointer_sprite_1[0] = framePointer 
        pointer_sprite_2[0] = framePointer
        pointer_sprite_3[0] = framePointer
        pointer_left_sprite[0] = framePointer
        framePointer = (framePointer + 1) % (pointer_sheet.width // 14)

        back_button_sprite[0] = frameBackButton
        frameBackButton = (frameBackButton + 1) % (back_button_sheet.width // 14)


        if charging:
            hackamon_sprite_charging[0] = frame 

        hackamon_sprite_idle[0] = frame
        frame = (frame + 1) % (hackamon_sheet_idle.width // tile_width)

        time.sleep(0.1)
        await asyncio.sleep(0)

asyncio.run(main())