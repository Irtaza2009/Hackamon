import pygame
import time
import random
import math
import asyncio

pygame.init()

screen = pygame.display.set_mode((128, 128))

splash = pygame.Surface((128, 128))

font = pygame.font.Font("PixelifySans-Regular.bdf", 12)

desk_bg_sprite = pygame.image.load("Desk-BG.bmp")
station_bg_sprite = pygame.image.load("Station-BG.bmp")
breakout_bg_sprite = pygame.image.load("Breakout-BG.bmp")
splash.blit(desk_bg_sprite, (0, 0))

tile_width = 32
tile_height = 32

brick_height = 8
brick_width = 16

hackamon_sheet_idle = pygame.image.load("Hackamon-1-Idle-Spritesheet.bmp")
hackamon_sprite_idle = hackamon_sheet_idle.subsurface(pygame.Rect(0, 0, tile_width, tile_height))

hackamon_sheet_jump = pygame.image.load("Hackamon-1-Jump-Spritesheet.bmp")
hackamon_sprite_jump = hackamon_sheet_jump.subsurface(pygame.Rect(0, 0, tile_width, tile_height))

hackamon_sheet_charging = pygame.image.load("Hackamon-1-Charging-Spritesheet.bmp")
hackamon_sprite_charging = hackamon_sheet_charging.subsurface(pygame.Rect(0, 0, tile_width, tile_height))

button_1_sheet = pygame.image.load("Button-1-Spritesheet.bmp")
button_1_sprite = button_1_sheet.subsurface(pygame.Rect(0, 0, 16, 18))

button_2_sheet = pygame.image.load("Button-2-Spritesheet.bmp")
button_2_sprite = button_2_sheet.subsurface(pygame.Rect(0, 0, 16, 18))

button_3_sheet = pygame.image.load("Button-3-Spritesheet.bmp")
button_3_sprite = button_3_sheet.subsurface(pygame.Rect(0, 0, 16, 18))

happiness_bar_sheet = pygame.image.load("Happiness-Bar-Spritesheet.bmp")
happiness_bar_sprite = happiness_bar_sheet.subsurface(pygame.Rect(0, 0, 48, 10))

battery_bar_sheet = pygame.image.load("Battery-Bar-Spritesheet.bmp")
battery_bar_sprite = battery_bar_sheet.subsurface(pygame.Rect(0, 0, 48, 10))

splash.blit(happiness_bar_sprite, (5, 8))
splash.blit(battery_bar_sprite, (5, 20))

splash.blit(button_1_sprite, ((screen.get_width() - tile_width) // 3, screen.get_height() - tile_height - 30))
splash.blit(button_2_sprite, ((screen.get_width() - tile_width) // 2 + 10, screen.get_height() - tile_height - 30))
splash.blit(button_3_sprite, ((screen.get_width() - tile_width) // 2 + 40, screen.get_height() - tile_height - 30))

charging_station_sheet = pygame.image.load("Charging-Station.bmp")
charging_station_sprite = charging_station_sheet.subsurface(pygame.Rect(0, 0, 55, 42))

pointer_sheet = pygame.image.load("Pointer-Spritesheet-2x.bmp")
pointer_sprite_1 = pointer_sheet.subsurface(pygame.Rect(0, 0, 14, 12))
pointer_sprite_2 = pointer_sheet.subsurface(pygame.Rect(0, 0, 14, 12))
pointer_sprite_3 = pointer_sheet.subsurface(pygame.Rect(0, 0, 14, 12))

splash.blit(pointer_sprite_1, (button_1_sprite.get_rect().centerx - 7, button_1_sprite.get_rect().top - 9))
splash.blit(pointer_sprite_2, (button_2_sprite.get_rect().centerx - 7, button_2_sprite.get_rect().top - 9))
splash.blit(pointer_sprite_3, (button_3_sprite.get_rect().centerx - 7, button_3_sprite.get_rect().top - 9))

brick_sheet = pygame.image.load("Breakout-Bricks-Spritesheet.bmp")
ball_sheet = pygame.image.load("Breakout-Ball.bmp")

splash.blit(hackamon_sprite_idle, (screen.get_width() // 2 - tile_width // 2, screen.get_height() - tile_height - 40))

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

happiness_label = font.render(str(happiness), True, (0, 0, 0))
battery_label = font.render(str(battery), True, (0, 0, 0))

splash.blit(happiness_label, (happiness_bar_sprite.get_rect().centerx - happiness_label.get_width() // 2, happiness_bar_sprite.get_rect().top + 2))
splash.blit(battery_label, (battery_bar_sprite.get_rect().centerx - battery_label.get_width() // 2, battery_bar_sprite.get_rect().top + 2))

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
        brick_sprite = pygame.Surface((brick_width, brick_height))
        brick_sprite.fill((255, 0, 0))  # Color the brick red
        brick_sprite.set_colorkey((0, 0, 0))  # Transparent background for the brick
        brick_sprite.rect = brick_sprite.get_rect(
            x=column * brick_width + 11 + column * 2,
            y=row * brick_height + 9 + row * 2
        )
        brick_sprites.append(brick_sprite)

# Ball for breakout
ball_sprite = pygame.Surface((6, 6))
ball_sprite.fill((0, 255, 0))  # Color the ball green
ball_sprite.rect = ball_sprite.get_rect(
    center=(pygame.display.get_surface().get_width() // 2, pygame.display.get_surface().get_height() // 2)
)

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

        happiness_label = pygame.font.SysFont('Arial', 24).render(
            str(happiness), True, (0, 0, 0)  # Black color
        )
        splash.append(happiness_label)

        battery_label = pygame.font.SysFont('Arial', 24).render(
            str(battery), True, (0, 0, 0)  # Black color
        )
        splash.append(battery_label)

def breakout():
    global ball_sprite, game_over, ball_delta_x, ball_delta_y, MAX_SPEED, RANDOM_RANGE, happiness
    ball_sprite.rect.y += round(ball_delta_y)
    ball_sprite.rect.x += round(ball_delta_x)

    # Let's not make it impossible so capping the speed
    ball_delta_x = max(min(ball_delta_x * 1.01, MAX_SPEED), -MAX_SPEED)
    ball_delta_y = max(min(ball_delta_y * 1.01, MAX_SPEED), -MAX_SPEED)

    if ball_sprite.rect.y > 128 - 10 - 6:
        ball_sprite.rect.y = hackamon_sprite_idle.rect.y
        ball_sprite.rect.x = hackamon_sprite_idle.rect.x + 16

    if ball_sprite.rect.y <= 0 + 7:
        ball_delta_y = -ball_delta_y  

    if ball_sprite.rect.x >= 128 - 6 - 6:
        ball_delta_x = -ball_delta_x

    if ball_sprite.rect.x <= 0 + 6:   
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


    button_2_sprite.rect.x = 16 + 10
    button_2_sprite.rect.y = 128 - 18 - 10
    button_2_sprite[0] = 0

    pointer_sprite_1.rect.x = button_2_sprite.rect.x + 16 // 2 - 14 // 2
    pointer_sprite_1.rect.y = button_2_sprite.rect.y - 9

    hackamon_sprite_idle.rect.x = screen.get_width() // 2 - tile_width // 2
    hackamon_sprite_idle.rect.y = 118 - tile_height
    hackamon_sprite_jump.rect.x = screen.get_width() // 2 - tile_width // 2
    hackamon_sprite_jump.rect.y = 118 - tile_height




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

    button_2_sprite.rect.x = 16 + 10
    button_2_sprite.rect.y = 128 - 18 - 10
    button_2_sprite[0] = 0

    splash.append(pointer_sprite_1)
    splash.append(pointer_sprite_2)

    splash.append(hackamon_sprite_idle)

    pointer_sprite_1.rect.x = button_2_sprite.rect.x + 16 // 2 - 14 // 2
    pointer_sprite_1.rect.y = button_2_sprite.rect.y - 9

    pointer_sprite_2.rect.x = charging_station_sprite.rect.x + 55 // 2 - 14 // 2
    pointer_sprite_2.rect.y = charging_station_sprite.rect.y + 42 // 2 - 18 // 2

    hackamon_sprite_idle.rect.x = 10
    hackamon_sprite_idle.rect.y = 128 - tile_height - 10
    hackamon_sprite_jump.rect.x = 10
    hackamon_sprite_jump.rect.y = 128 - tile_height - 10

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
   

    button_2_sprite.rect.x = (screen.get_width() - tile_width) // 2 + 10
    button_2_sprite.rect.y = screen.get_height() - tile_height - 30

    button_1_sprite[0] = 0
    button_2_sprite[0] = 0
    button_3_sprite[0] = 0

    splash.append(pointer_sprite_1)
    splash.append(pointer_sprite_2)
    splash.append(pointer_sprite_3)

    pointer_sprite_1.rect.x = button_1_sprite.rect.x + 16 // 2 - 14 // 2
    pointer_sprite_1.rect.y = button_1_sprite.rect.y - 9
    pointer_sprite_2.rect.x = button_2_sprite.rect.x + 16 // 2 - 14 // 2
    pointer_sprite_2.rect.y = button_2_sprite.rect.y - 9
    pointer_sprite_3.rect.x = button_3_sprite.rect.x + 16 // 2 - 14 // 2
    pointer_sprite_3.rect.y = button_3_sprite.rect.y - 9


    splash.append(hackamon_sprite_idle)

    hackamon_sprite_idle.rect.x = (screen.get_width() - tile_width) // 2
    hackamon_sprite_idle.rect.y = screen.get_height() - tile_height - 40
    hackamon_sprite_jump.rect.x = (screen.get_width() - tile_width) // 2
    hackamon_sprite_jump.rect.y = screen.get_height() - tile_height - 40


async def main():
    global frame, framePointer, isJumping, facing_left, gameState, charging, chargingSprite
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if screen.check_quit():
            break



        keys = pygame.key.get_pressed()

        if game_over == False:
            if keys[pygame.K_LEFT]:
                charging = False
                if (gameState == "Main" and hackamon_sprite_idle.rect.x > 24) or (gameState == "Station" and hackamon_sprite_idle.rect.x > 0) or (gameState == "Breakout" and hackamon_sprite_idle.rect.x > 0):
                    facing_left = True
                    hackamon_sprite_idle.rect.x -= speed
                    hackamon_sprite_jump.rect.x -= speed
                    hackamon_sprite_idle.flip_x = False
                    hackamon_sprite_jump.flip_x = False

            if keys[pygame.K_RIGHT]:
                charging = False
                if (gameState == "Main" and hackamon_sprite_idle.rect.x < 78) or (gameState == "Station" and hackamon_sprite_idle.rect.x < 128 - tile_width) or (gameState == "Breakout" and hackamon_sprite_idle.rect.x < 128 - tile_width):
                    facing_left = False
                    hackamon_sprite_idle.rect.x += speed
                    hackamon_sprite_jump.rect.x += speed
                    hackamon_sprite_idle.flip_x = True
                    hackamon_sprite_jump.flip_x = True

            # For testing! I know there will be only 3 buttons :)
            if keys[pygame.K_UP]:
                charging = False
                if (gameState == "Main" and hackamon_sprite_idle.rect.y > 64 - 20) or (gameState == "Station" and hackamon_sprite_idle.rect.y > 96 - 20):
                    hackamon_sprite_idle.rect.y -= speed
                    hackamon_sprite_jump.rect.y -= speed
                    
            if keys[pygame.K_DOWN]:
                charging = False
                if (gameState == "Main" and hackamon_sprite_idle.rect.y < 92 - tile_height) or (gameState == "Station" and hackamon_sprite_idle.rect.y < 128 - tile_height):
                    hackamon_sprite_idle.rect.y += speed
                    hackamon_sprite_jump.rect.y += speed
            
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
                hackamon_sprite_idle.rect.x = 128 - tile_width - 10
                hackamon_sprite_idle.rect.y = 128 - tile_height - 10
                hackamon_sprite_jump.rect.x = 128 - tile_width - 10
                hackamon_sprite_jump.rect.y = 128 - tile_height - 10

            if gameState == "Breakout":
                breakout()

            manage_stats()

            


        
        pointer_sprite_1[0] = framePointer 
        pointer_sprite_2[0] = framePointer
        pointer_sprite_3[0] = framePointer
        framePointer = (framePointer + 1) % (pointer_sheet.get_width() // 14)


        if charging:
            hackamon_sprite_charging[0] = frame 

        hackamon_sprite_idle[0] = frame
        frame = (frame + 1) % (hackamon_sheet_idle.get_width() // tile_width)

        time.sleep(0.1)
        await asyncio.sleep(0)

asyncio.run(main())
