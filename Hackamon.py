import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
import pygame
#import asyncio
import time
import math
import random




class Hackamon:

    def __init__(self, display, splash):

        #pygame.init()
        
    
    
        # test leaderboard data
        self.leaderboard_data = [
            {"username": "Irtaza", "pet_level": 6},
            {"username": "Test", "pet_level": 4},
            {"username": "Pet", "pet_level": 3},
            {"username": "Childe", "pet_level": 2},
            {"username": "Robo", "pet_level": 1}
        ]

        self.display = display
        
        self.splash = splash
        self.display.show(self.splash)

        self.splash.pop()

        

        self.font = bitmap_font.load_font("fonts/PixelifySans-Regular.bdf")
        self.card_font = bitmap_font.load_font("fonts/PixelifySans-Regular-8px.bdf")
        self.font24px = bitmap_font.load_font("fonts/PixelifySans-Regular-24px.bdf")

        self.desk_background = displayio.OnDiskBitmap("assets/Desk-BG.bmp")
        self.desk_bg_sprite = displayio.TileGrid(self.desk_background, pixel_shader=self.desk_background.pixel_shader)
        self.station_background = displayio.OnDiskBitmap("assets/Station-BG.bmp")
        self.station_bg_sprite = displayio.TileGrid(self.station_background, pixel_shader=self.station_background.pixel_shader)
        self.breakout_background = displayio.OnDiskBitmap("assets/Breakout-BG.bmp")
        self.breakout_bg_sprite = displayio.TileGrid(self.breakout_background, pixel_shader=self.breakout_background.pixel_shader)
        self.leaderboard_background = displayio.OnDiskBitmap("assets/Leaderboard-BG.bmp")
        self.leaderboard_bg_sprite = displayio.TileGrid(self.leaderboard_background, pixel_shader=self.leaderboard_background.pixel_shader)
        self.splash.append(self.desk_bg_sprite)

        self.tile_width = 32
        self.tile_height = 32

        self.brick_height = 8
        self.brick_width = 16

        self.hackamon_sheet_idle = displayio.OnDiskBitmap("assets/Hackamon-1-Idle-Spritesheet.bmp")
        self.hackamon_sprite_idle = displayio.TileGrid(self.hackamon_sheet_idle,
                                            pixel_shader=self.hackamon_sheet_idle.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=self.tile_width,
                                            tile_height=self.tile_height,
                                            default_tile=0,
                                            x=(self.display.width - self.tile_width) // 2,
                                            y=self.display.height - self.tile_height - 40)


        self.hackamon_sheet_jump = displayio.OnDiskBitmap("assets/Hackamon-1-Jump-Spritesheet.bmp")
        self.hackamon_sprite_jump = displayio.TileGrid(self.hackamon_sheet_jump,
                                                pixel_shader=self.hackamon_sheet_jump.pixel_shader,
                                                width=1,
                                                height=1,
                                                tile_width=self.tile_width,
                                                tile_height=self.tile_height,
                                                default_tile=0,
                                                x=(self.display.width - self.tile_width) // 2,
                                                y=self.display.height - self.tile_height - 40)

        self.hackamon_sheet_charging = displayio.OnDiskBitmap("assets/Hackamon-1-Charging-Spritesheet.bmp")
        self.hackamon_sprite_charging = displayio.TileGrid(self.hackamon_sheet_charging,
                                                pixel_shader=self.hackamon_sheet_charging.pixel_shader,
                                                width=1,
                                                height=1,
                                                tile_width=self.tile_width,
                                                tile_height=self.tile_height,
                                                default_tile=0,
                                                x=85,
                                                y=70)

        self.button_1_sheet = displayio.OnDiskBitmap("assets/Button-1-Spritesheet.bmp")

        self.button_1_sprite = displayio.TileGrid(self.button_1_sheet,
                                            pixel_shader=self.button_1_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=16,
                                            tile_height=18,
                                            default_tile=0,
                                            x=(self.display.width - self.tile_width) // 3,
                                            y=self.display.height - self.tile_height - 30)

        self.button_2_sheet = displayio.OnDiskBitmap("assets/Button-2-Spritesheet.bmp")

        self.button_2_sprite = displayio.TileGrid(self.button_2_sheet,
                                            pixel_shader=self.button_2_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=16,
                                            tile_height=18,
                                            default_tile=0,
                                            x=(self.display.width - self.tile_width) // 2 + 10,
                                            y=self.display.height - self.tile_height - 30)

        self.button_3_sheet = displayio.OnDiskBitmap("assets/Button-3-Spritesheet.bmp")

        self.button_3_sprite = displayio.TileGrid(self.button_3_sheet,
                                            pixel_shader=self.button_3_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=16,
                                            tile_height=18,
                                            default_tile=0,
                                            x=(self.display.width - self.tile_width) // 2 + 40,
                                            y=self.display.height - self.tile_height - 30)

        self.back_button_sheet = displayio.OnDiskBitmap("assets/Back-Button-Spritesheet.bmp")
        self.back_button_sprite = displayio.TileGrid(self.back_button_sheet,
                                            pixel_shader=self.back_button_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=14,
                                            tile_height=10,
                                            default_tile=0,
                                            x=10,
                                            y=10)

        self.happiness_bar_sheet = displayio.OnDiskBitmap("assets/Happiness-Bar-Spritesheet.bmp")

        self.happiness_bar_sprite = displayio.TileGrid(self.happiness_bar_sheet,
                                            pixel_shader=self.happiness_bar_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=48,
                                            tile_height=10,
                                            default_tile=0,
                                            x=5,
                                            y=8)

        self.splash.append(self.happiness_bar_sprite)



        self.battery_bar_sheet = displayio.OnDiskBitmap("assets/Battery-Bar-Spritesheet.bmp")

        self.battery_bar_sprite = displayio.TileGrid(self.battery_bar_sheet,
                                            pixel_shader=self.battery_bar_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=48,
                                            tile_height=10,
                                            default_tile=0,
                                            x=5,
                                            y=20)

        self.splash.append(self.battery_bar_sprite)

        self.day_night_cycle_bar_sheet = displayio.OnDiskBitmap("assets/Day-Night-Bar-Spritesheet.bmp")
        self.day_night_cycle_bar_sprite = displayio.TileGrid(self.day_night_cycle_bar_sheet,
                                            pixel_shader=self.day_night_cycle_bar_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=48,
                                            tile_height=10,
                                            default_tile=0,
                                            x=5,
                                            y=32)

        self.splash.append(self.day_night_cycle_bar_sprite)

        self.splash.append(self.button_1_sprite)

        self.splash.append(self.button_2_sprite)

        self.splash.append(self.button_3_sprite)

        self.charging_station_sheet = displayio.OnDiskBitmap("assets/Charging-Station.bmp")
        self.charging_station_sprite = displayio.TileGrid(self.charging_station_sheet,
                                            pixel_shader=self.charging_station_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=55,
                                            tile_height=42,
                                            default_tile=0,
                                            x=72,
                                            y=70)


        self.pointer_sheet = displayio.OnDiskBitmap("assets/Pointer-Spritesheet-2x.bmp")
        self.pointer_sprite_1 = displayio.TileGrid(self.pointer_sheet,
                                                width=1,
                                                pixel_shader=self.pointer_sheet.pixel_shader,
                                                height=1,
                                                tile_width=14,
                                                tile_height=12,
                                                default_tile=0,
                                                x=self.button_1_sprite.x + 16 // 2 - 14 // 2,
                                                y=self.button_1_sprite.y - 9)
        self.pointer_sprite_2 = displayio.TileGrid(self.pointer_sheet,
                                                width=1,
                                                pixel_shader=self.pointer_sheet.pixel_shader,
                                                height=1,
                                                tile_width=14,
                                                tile_height=12,
                                                default_tile=0,
                                                x=self.button_2_sprite.x + 16 // 2 - 14 // 2,
                                                y=self.button_2_sprite.y - 9)
        self.pointer_sprite_3 = displayio.TileGrid(self.pointer_sheet,
                                                width=1,
                                                pixel_shader=self.pointer_sheet.pixel_shader,
                                                height=1,
                                                tile_width=14,
                                                tile_height=12,
                                                default_tile=0,
                                                x=self.button_3_sprite.x + 16 // 2 - 14 // 2,
                                                y=self.button_3_sprite.y - 9)

        self.pointer_left_sheet = displayio.OnDiskBitmap("assets/Pointer-Left-Spritesheet-2x.bmp")
        self.pointer_left_sprite = displayio.TileGrid(self.pointer_left_sheet,
                                                width=1,
                                                pixel_shader=self.pointer_sheet.pixel_shader,
                                                height=1,
                                                tile_width=14,
                                                tile_height=12,
                                                default_tile=0,
                                                x=10,
                                                y=10)

        self.splash.append(self.pointer_sprite_1)
        self.splash.append(self.pointer_sprite_2)
        self.splash.append(self.pointer_sprite_3)

        self.player_card_sheet = displayio.OnDiskBitmap("assets/Player-Card-Spritesheet.bmp")
        self.player_card_sprite = displayio.TileGrid(self.player_card_sheet,
                                            pixel_shader=self.player_card_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=100,
                                            tile_height=20,
                                            default_tile=0,
                                            x=14,
                                            y=5)

                                        


        self.brick_sheet = displayio.OnDiskBitmap("assets/Breakout-Bricks-Spritesheet.bmp")
        self.ball_sheet = displayio.OnDiskBitmap("assets/Breakout-Ball.bmp")

        self.splash.append(self.hackamon_sprite_idle)

        self.frame = 0
        self.framePointer = 0
        self.frameBackButton = 0
        self.speed = 4
        self.game_over = False
        self.isJumping = False
        self.facing_left = True
        self.gameState = "Main"
        self.happiness = 5000
        self.battery = 5000
        self.day_night = 5000
        self.day = 0
        self.level = 0
        self.charging = False
        self.chargingSprite = False
        self.ball_delta_x = 1
        self.ball_delta_y = 1
        self.MAX_SPEED = 3  # Maximum ball speed
        self.RANDOM_RANGE = 1  # Random range for offsetting ball direction



        self.happiness_label = label.Label(
            self.font,
            text=str(self.happiness),
            color=0x000000,  # Black color
            anchor_point=(0.5, 0),
            anchored_position=(self.happiness_bar_sprite.x + 28, self.happiness_bar_sprite.y + 2)
        )

        self.splash.append(self.happiness_label)

        self.battery_label = label.Label(
            self.font,
            text=str(self.battery),
            color=0x000000,  # Black color
            anchor_point=(0.5, 0),
            anchored_position=(self.battery_bar_sprite.x + 28, self.battery_bar_sprite.y + 2)
        )

        self.splash.append(self.battery_label)

        self.level_label = label.Label(
            self.font24px,
            text="Level: " + str(self.level),
            color=0xFFFFFF,
            anchor_point=(0.5, 0.5),
            anchored_position=(self.display.width // 2, self.display.height // 2)
        )

            # Bricks for breakout

        self.brick_sprites = []
        self.rows = 4
        self.columns = 6

        for row in range(self.rows):
            for column in range(self.columns):
                brick_sprite = displayio.TileGrid(self.brick_sheet,
                                            pixel_shader=self.brick_sheet.pixel_shader,
                                            width=1,
                                            height=1,
                                            tile_width=self.brick_width,
                                            tile_height=self.brick_height,
                                            default_tile=0,
                                            x=column * self.brick_width + 11 + column * 2,
                                            y=row * self.brick_height + 9 + row * 2)
                brick_sprite[0] = column
                self.brick_sprites.append(brick_sprite)

        # Ball for breakout

        self.ball_sprite = displayio.TileGrid(self.ball_sheet,
                                        pixel_shader=self.ball_sheet.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=6,
                                        tile_height=6,
                                        default_tile=0,
                                        x=(self.display.width - 6) // 2,
                                        y=self.display.height // 2)



    def run_jump_animation(self):   
        #global frame, isJumping

        

        for self.jump_frame in range(self.hackamon_sheet_jump.width // self.tile_width):

            self.hackamon_sprite_jump[0] = self.jump_frame
            time.sleep(0.1)

        

        self.splash.remove(self.hackamon_sprite_jump)
        self.splash.append(self.hackamon_sprite_idle)
        self.isJumping = False

    # Collision function
    def check_collision(sprite1, sprite2, width1, height1, width2, height2):
        return (
            sprite1.x < sprite2.x + width2 and
            sprite1.x + width1 > sprite2.x and
            sprite1.y < sprite2.y + height2 and
            sprite1.y + height1 > sprite2.y
        )

    def check_button_press(self):
        #global gameState
        print("Checking Button Press...")
        # Using the dimensions of the button and sprite for accurate detection (todo: create variables for these)
        if self.check_collision(
            self.hackamon_sprite_idle, self.button_1_sprite,
            self.tile_width, self.tile_height, 16, 18
        ) and self.gameState == "Main":
            self.button_1_sprite[0] = 1  
            print("Button Pressed!")
            time.sleep(0.5)
            self.gameState = "Station"
            self.to_charging_station(self)
        elif self.check_collision(
            self.hackamon_sprite_idle, self.button_2_sprite,
            self.tile_width, self.tile_height, 16, 18
        ) and self.gameState == "Main":
            self.button_2_sprite[0] = 1
            self.to_leaderboard(self)
        elif self.check_collision(
            self.hackamon_sprite_idle, self.button_2_sprite,
            self.tile_width, self.tile_height, 16, 18
        ) and (self.gameState == "Station" or self.gameState == "Breakout"):
            self.button_2_sprite[0] = 1
            print("Button Pressed!")
            time.sleep(0.5)
            self.to_main(self, self.gameState)
        elif self.check_collision(
            self.hackamon_sprite_idle, self.button_3_sprite,
            self.tile_width, self.tile_height, 16, 18
        ) and self.gameState == "Main":
            self.button_3_sprite[0] = 1
            print("Button Pressed!")
            time.sleep(0.5)
            self.gameState = "Breakout"
            self.to_breakout(self)

    def charging_station(self):
        #global battery, facing_left, charging, chargingSprite
        if self.check_collision(
            self.hackamon_sprite_idle, self.charging_station_sprite,
            self.tile_width, self.tile_height, 55, 42
        ):
            print("Charging!")
            if self.facing_left == False:
                self.facing_left = True
                self.hackamon_sprite_idle.flip_x = False
                self.hackamon_sprite_jump.flip_x = False

            self.splash.append(self.hackamon_sprite_charging)


            self.hackamon_sprite_idle.x = 85
            self.hackamon_sprite_idle.y = 70
            self.hackamon_sprite_jump.x = 85
            self.hackamon_sprite_jump.y = 70
            self.charging = True
            self.chargingSprite = True




    def manage_stats(self):
        #global happiness, battery, game_over, charging, happiness_label, battery_label, level_label, day_night, day, level
        
        if self.happiness <= 0 or self.battery <= 0:
            print("Game Over!")
            self.to_main(self, gameState)
            self.game_over = True
        else:
            self.happiness -= 1
            #print("Happiness: " + str(happiness))
            self.happiness_bar_sprite[0] = 4 - math.ceil(self.happiness // 1000)
            if self.charging:
                if self.battery < 4999:
                    self.battery += 1
                elif self.battery == 4999:
                    self.charging = False
            else:
                self.battery -= 1
            #print("Battery: " + str(battery))
            self.battery_bar_sprite[0] = 4 - math.ceil(self.battery // 1000)

        if self.gameState != "Breakout" and self.gameState != "Leaderboard":
            self.splash.remove(self.happiness_label)
            self.splash.remove(self.battery_label)

            self.happiness_label = label.Label(
                self.font,
                text=str(self.happiness),
                color=0x000000,  # Black color
                anchor_point=(0.5, 0),
                anchored_position=(self.happiness_bar_sprite.x + 28, self.happiness_bar_sprite.y + 2)
            )
            self.splash.append(self.happiness_label)

            self.battery_label = label.Label(
            self.font,
            text=str(self.battery),
            color=0x000000,  # Black color
            anchor_point=(0.5, 0),
            anchored_position=(self.battery_bar_sprite.x + 28, self.battery_bar_sprite.y + 2)
            )

            self.splash.append(self.battery_label)

        
        if self.day_night == 0:
            self.day += 1
            self.day_night = 4900
            self.level += 1


            level_label = label.Label(
                self.font24px,
                text="Level: " + str(self.level),
                color=0xFFFFFF,
                anchor_point=(0.5, 0.5),
                anchored_position=(self.display.width // 2, self.display.height // 2)
            )

            background_rect = Rect(2, 50, 126, 30, fill=0x222034)
        
            # Append the rectangle and the label to the splash group
            self.splash.append(background_rect)

            self.splash.append(level_label)
            time.sleep(2)
            self.splash.remove(level_label)
            self.splash.remove(background_rect)

        else:
            self.day_night -= 20

            self.day_night_cycle_bar_sprite[0] = 4 - math.ceil(self.day_night // 1000)

            
    def breakout(self):
        #global ball_sprite, game_over, ball_delta_x, ball_delta_y, MAX_SPEED, RANDOM_RANGE, happiness
        self.ball_sprite.y += round(self.ball_delta_y)
        self.ball_sprite.x += round(self.ball_delta_x)

        # Let's not make it impossible so capping the speed

        self.ball_delta_x = max(min(self.ball_delta_x * 1.01, self.MAX_SPEED), -self.MAX_SPEED)
        self.ball_delta_y = max(min(self.ball_delta_y * 1.01, self.MAX_SPEED), -self.MAX_SPEED)

        if self.ball_sprite.y > 128 - 10 - 6:
            self.ball_sprite.y = self.hackamon_sprite_idle.y 
            self.ball_sprite.x = self.hackamon_sprite_idle.x + 16

        if self.ball_sprite.y <= 0 + 7:
            self.ball_delta_y = -self.ball_delta_y  

        if self.ball_sprite.x >= 128 - 6 - 6:
            self.ball_delta_x = -self.ball_delta_x

        if self.ball_sprite.x <= 0 + 6:   
            self.ball_delta_x = -self.ball_delta_x

        if self.check_collision(
            self.ball_sprite, self.hackamon_sprite_idle,
            6, 6, self.tile_width, self.tile_height
        ):
            print("Ball Hit Hackamon!")
            self.ball_delta_y = -self.ball_delta_y 
            self.ball_delta_x = -self.ball_delta_x + random.randint(-self.RANDOM_RANGE, self.RANDOM_RANGE)

        for brick in self.brick_sprites:
            if self.check_collision(
                self.ball_sprite, brick,
                6, 6, self.brick_width, self.brick_height
            ):
                print("Ball Hit Brick!")
                self.brick_sprites.remove(brick)
                self.splash.remove(brick)
                self.ball_delta_y = -self.ball_delta_y + random.randint(-self.RANDOM_RANGE, self.RANDOM_RANGE)
                self.ball_delta_x = -self.ball_delta_x 
                if self.happiness < 4959:
                    self.happiness += 40

        # Ensuring ball direction remains within bounds after adding random direction offset
        self.ball_delta_x = max(min(self.ball_delta_x, self.MAX_SPEED), -self.MAX_SPEED)
        self.ball_delta_y = max(min(self.ball_delta_y, self.MAX_SPEED), -self.MAX_SPEED)

        if len(self.brick_sprites) == 0:
            print("Game Won!")
            if self.happiness < 4000:
                self.happiness += 1000
            else:
                self.happiness = 4999
            self.to_main(self.gameState)


    # player data in leaderboard


    player_card_sprites = []
    player_card_usernames = []
    player_card_pet_levels = []

    def create_player_card(self, username, pet_level, x, y):             
        player_card_sprite = displayio.TileGrid(self.player_card_sheet,
                                        pixel_shader=self.player_card_sheet.pixel_shader,
                                        width=1,
                                        height=1,
                                        tile_width=100,
                                        tile_height=20,
                                        default_tile=0,
                                        x=x,
                                        y=y)
        username_label = label.Label(self.card_font, text=username, color=0x7a8af0, anchor_point=(0, 0), anchored_position=(x + 5, y + 7))
        pet_level_label = label.Label(self.card_font, text="Lvl: " + str(pet_level), color=0x3f3f74, anchor_point=(0, 0), anchored_position=(x + 65, y + 7))
        
        
        player_card_sprite[0] = (y - 10) / 22

        self.player_card_sprites.append(player_card_sprite)
        self.player_card_usernames.append(username_label)
        self.player_card_pet_levels.append(pet_level_label)

        self.splash.append(player_card_sprite)
        self.splash.append(username_label)
        self.splash.append(pet_level_label)

    # Functions to switch between game states

    def to_leaderboard(self):
        #global gameState
        self.gameState = "Leaderboard"
        # remove all from splash
        self.splash.remove(self.hackamon_sprite_idle)
        self.splash.remove(self.desk_bg_sprite)
        self.splash.remove(self.button_1_sprite)
        self.splash.remove(self.button_2_sprite)
        self.splash.remove(self.button_3_sprite)
        self.splash.remove(self.happiness_bar_sprite)
        self.splash.remove(self.battery_bar_sprite)
        self.splash.remove(self.day_night_cycle_bar_sprite)
        self.splash.remove(self.pointer_sprite_1)
        self.splash.remove(self.pointer_sprite_2)
        self.splash.remove(self.pointer_sprite_3)

        # leaderboard background and sprites
        self.splash.append(self.leaderboard_bg_sprite)
        # player cards for the leaderboard
        y_position = 10
        for player in self.leaderboard_data:
            self.create_player_card(self, player['username'], player['pet_level'], 14, y_position)
            y_position += 20 + 2
        #splash.append(back_button_sprite)
        self.splash.append(self.pointer_sprite_1)
        self.splash.append(self.pointer_sprite_2)
        self.splash.append(self.pointer_left_sprite)

        self.pointer_sprite_1.x = 24 - 14 // 2
        self.pointer_sprite_1.y = 128 - 10
        self.pointer_sprite_2.x = 128 - 24 - 14 // 2
        self.pointer_sprite_2.y = 128 - 10
        self.pointer_sprite_2.flip_y = True
        self.pointer_left_sprite.x = 128 // 2 - 14 // 2
        self.pointer_left_sprite.y = 128 - 10

        #back_button_sprite.x = 128 // 2 - 14 // 2
        #back_button_sprite.y = 128 - 10 



    def to_breakout(self):
        global gameState
        gameState = "Breakout"
        # remove all from splash
        self.splash.remove(self.hackamon_sprite_idle)
        self.splash.remove(self.desk_bg_sprite)
        self.splash.remove(self.button_1_sprite)
        self.splash.remove(self.button_2_sprite)
        self.splash.remove(self.button_3_sprite)
        self.splash.remove(self.happiness_bar_sprite)
        self.splash.remove(self.battery_bar_sprite)
        self.splash.remove(self.day_night_cycle_bar_sprite)
        self.splash.remove(self.pointer_sprite_1)
        self.splash.remove(self.pointer_sprite_2)
        self.splash.remove(self.pointer_sprite_3)
        
        # add breakout background and sprites
        self.splash.append(self.breakout_bg_sprite)
        self.splash.append(self.button_2_sprite)
        for brick in self.brick_sprites:
            self.splash.append(brick)
        self.splash.append(self.pointer_sprite_1)
        self.splash.append(self.hackamon_sprite_idle)
        self.splash.append(self.ball_sprite)


        

        self.button_2_sprite.x = 16 + 10
        self.button_2_sprite.y = 128 - 18 - 10
        self.button_2_sprite[0] = 0

        self.pointer_sprite_1.x = self.button_2_sprite.x + 16 // 2 - 14 // 2
        self.pointer_sprite_1.y = self.button_2_sprite.y - 9

        self.hackamon_sprite_idle.x = self.display.width // 2 - self.tile_width // 2
        self.hackamon_sprite_idle.y = 118 - self.tile_height
        self.hackamon_sprite_jump.x = self.display.width // 2 - self.tile_width // 2
        self.hackamon_sprite_jump.y = 118 - self.tile_height




    def to_charging_station(self):
        #global gameState
        self.gameState = "Station"
        # remove all from splash
        self.splash.remove(self.hackamon_sprite_idle)
        self.splash.remove(self.button_1_sprite)
        self.splash.remove(self.button_2_sprite)
        self.splash.remove(self.button_3_sprite)
        self.splash.remove(self.happiness_bar_sprite)
        self.splash.remove(self.battery_bar_sprite)
        self.splash.remove(self.day_night_cycle_bar_sprite)
        self.splash.remove(self.desk_bg_sprite)
        self.splash.remove(self.pointer_sprite_1)
        self.splash.remove(self.pointer_sprite_2)
        self.splash.remove(self.pointer_sprite_3)
        # add station background and sprites back
        self.splash.append(self.station_bg_sprite)
        self.splash.append(self.charging_station_sprite)
        self.splash.append(self.happiness_bar_sprite)
        self.splash.append(self.day_night_cycle_bar_sprite)
        self.splash.append(self.battery_bar_sprite)
        self.splash.append(self.button_2_sprite)

        self.button_2_sprite.x = 16 + 10
        self.button_2_sprite.y = 128 - 18 - 10
        self.button_2_sprite[0] = 0

        self.splash.append(self.pointer_sprite_1)
        self.splash.append(self.pointer_sprite_2)

        self.splash.append(self.hackamon_sprite_idle)

        self.pointer_sprite_1.x = self.button_2_sprite.x + 16 // 2 - 14 // 2
        self.pointer_sprite_1.y = self.button_2_sprite.y - 9

        self.pointer_sprite_2.x = self.charging_station_sprite.x + 55 // 2 - 14 // 2
        self.pointer_sprite_2.y = self.charging_station_sprite.y + 42 // 2 - 18 // 2

        self.hackamon_sprite_idle.x = 10
        self.hackamon_sprite_idle.y = 128 - self.tile_height - 10
        self.hackamon_sprite_jump.x = 10
        self.hackamon_sprite_jump.y = 128 - self.tile_height - 10

    def to_main(self, prevGameState):
        #global gameState
        self.gameState = "Main"
        # remove all from splash

        if prevGameState == "Leaderboard":
            self.splash.remove(self.leaderboard_bg_sprite)
            for player_card in self.player_card_sprites:
                self.player_card_sprites.remove(player_card)
                self.splash.remove(player_card)
            for username in self.player_card_usernames:
                self.player_card_usernames.remove(username)
                self.splash.remove(username)
            for pet_level in self.player_card_pet_levels:
                self.player_card_pet_levels.remove(pet_level)
                self.splash.remove(pet_level)
            #splash.remove(back_button_sprite)
            self.splash.remove(self.pointer_sprite_1)
            self.pointer_sprite_2.flip_y = False
            self.splash.remove(self.pointer_sprite_2)
            self.splash.remove(self.pointer_left_sprite)
        else:

            # if from breakout
            if prevGameState == "Breakout":
                self.splash.remove(self.breakout_bg_sprite)
                for brick in self.brick_sprites:
                    self.splash.remove(brick)
                self.splash.remove(self.ball_sprite)
                self.splash.remove(self.pointer_sprite_1)
                
            self.splash.remove(self.hackamon_sprite_idle)

            # if from station
            if prevGameState == "Station": 
                self.splash.remove(self.charging_station_sprite)
                self.splash.remove(self.station_bg_sprite)
                self.splash.remove(self.happiness_bar_sprite)
                self.splash.remove(self.battery_bar_sprite)
                self.splash.remove(self.day_night_cycle_bar_sprite)
                self.splash.remove(self.pointer_sprite_1)
                self.splash.remove(self.pointer_sprite_2)
            self.splash.remove(self.button_2_sprite)

        # add main background and sprites back
        self.splash.append(self.desk_bg_sprite)
        self.splash.append(self.button_1_sprite)
        self.splash.append(self.button_2_sprite)
        self.splash.append(self.button_3_sprite)
        self.splash.append(self.happiness_bar_sprite)
        self.splash.append(self.battery_bar_sprite)
        self.splash.append(self.day_night_cycle_bar_sprite)
    

        self.button_2_sprite.x = (self.display.width - self.tile_width) // 2 + 10
        self.button_2_sprite.y = self.display.height - self.tile_height - 30

        self.button_1_sprite[0] = 0
        self.button_2_sprite[0] = 0
        self.button_3_sprite[0] = 0

        self.splash.append(self.pointer_sprite_1)
        self.splash.append(self.pointer_sprite_2)
        self.splash.append(self.pointer_sprite_3)

        self.pointer_sprite_1.x=self.button_1_sprite.x + 16 // 2 - 14 // 2
        self.pointer_sprite_1.y=self.button_1_sprite.y - 9
        self.pointer_sprite_2.x=self.button_2_sprite.x + 16 // 2 - 14 // 2
        self.pointer_sprite_2.y=self.button_2_sprite.y - 9
        self.pointer_sprite_3.x=self.button_3_sprite.x + 16 // 2 - 14 // 2
        self.pointer_sprite_3.y=self.button_3_sprite.y - 9


        self.splash.append(self.hackamon_sprite_idle)

        self.hackamon_sprite_idle.x = (self.display.width - self.tile_width) // 2
        self.hackamon_sprite_idle.y = self.display.height - self.tile_height - 40
        self.hackamon_sprite_jump.x = (self.display.width - self.tile_width) // 2
        self.hackamon_sprite_jump.y = self.display.height - self.tile_height - 40


    #async def main(self):
    def main(self):
        #global frame, framePointer, frameBackButton, isJumping, facing_left, gameState, charging, chargingSprite

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if self.display.check_quit():
                break



            keys = pygame.key.get_pressed()

            if self.game_over == False:
                if keys[pygame.K_LEFT]:
                    self.charging = False
                    if (self.gameState == "Main" and self.hackamon_sprite_idle.x > 24) or (self.gameState == "Station" and self.hackamon_sprite_idle.x > 0) or (self.gameState == "Breakout" and self.hackamon_sprite_idle.x > 0):
                        self.facing_left = True
                        self.hackamon_sprite_idle.x -= self.speed
                        self.hackamon_sprite_jump.x -= self.speed
                        self.hackamon_sprite_idle.flip_x = False
                        self.hackamon_sprite_jump.flip_x = False

                if keys[pygame.K_RIGHT]:
                    self.charging = False
                    if (self.gameState == "Main" and self.hackamon_sprite_idle.x < 78) or (self.gameState == "Station" and self.hackamon_sprite_idle.x < 128 - self.tile_width) or (self.gameState == "Breakout" and self.hackamon_sprite_idle.x < 128 - self.tile_width):
                        self.facing_left = False
                        self.hackamon_sprite_idle.x += self.speed
                        self.hackamon_sprite_jump.x += self.speed
                        self.hackamon_sprite_idle.flip_x = True
                        self.hackamon_sprite_jump.flip_x = True

                # For testing! I know there will be only 3 buttons :)
                if keys[pygame.K_UP]:
                    self.charging = False
                    if (self.gameState == "Main" and self.hackamon_sprite_idle.y > 64 - 20) or (self.gameState == "Station" and self.hackamon_sprite_idle.y > 96 - 20):
                        self.hackamon_sprite_idle.y -= self.speed
                        self.hackamon_sprite_jump.y -= self.speed
                        
                if keys[pygame.K_DOWN]:
                    self.charging = False
                    if (self.gameState == "Main" and self.hackamon_sprite_idle.y < 92 - self.tile_height) or (self.gameState == "Station" and self.hackamon_sprite_idle.y < 128 - self.tile_height):
                        self.hackamon_sprite_idle.y += self.speed
                        self.hackamon_sprite_jump.y += self.speed
                
                if keys[pygame.K_SPACE] and self.gameState == "Leaderboard":
                        time.sleep(0.5)
                        self.to_main(self, self.gameState)

                elif keys[pygame.K_SPACE] and not self.isJumping and not self.charging:        
                    self.isJumping = True
                    self.splash.remove(self.hackamon_sprite_idle)
                    self.splash.append(self.hackamon_sprite_jump)
                    self.run_jump_animation(self)
                    self.check_button_press(self)
                    if self.gameState == "Station":
                        self.charging_station(self)

                
                
                if self.chargingSprite == True and not self.charging:
                    self.chargingSprite = False
                    self.splash.remove(self.hackamon_sprite_charging)
                    self.hackamon_sprite_idle.x = 128 - self.tile_width - 10
                    self.hackamon_sprite_idle.y = 128 - self.tile_height - 10
                    self.hackamon_sprite_jump.x = 128 - self.tile_width - 10
                    self.hackamon_sprite_jump.y = 128 - self.tile_height - 10

                if self.gameState == "Breakout":
                    self.breakout(self)

                self.manage_stats(self)

                


            
            self.pointer_sprite_1[0] = self.framePointer 
            self.pointer_sprite_2[0] = self.framePointer
            self.pointer_sprite_3[0] = self.framePointer
            self.pointer_left_sprite[0] = self.framePointer
            self.framePointer = (self.framePointer + 1) % (self.pointer_sheet.width // 14)

            self.back_button_sprite[0] = self.frameBackButton
            self.frameBackButton = (self.frameBackButton + 1) % (self.back_button_sheet.width // 14)


            if self.charging:
                self.hackamon_sprite_charging[0] = self.frame 

            self.hackamon_sprite_idle[0] = self.frame
            self.frame = (self.frame + 1) % (self.hackamon_sheet_idle.width // self.tile_width)
            pygame.display.flip()

            time.sleep(0.1)
            #await asyncio.sleep(0)

    #asyncio.run(main())

if __name__ == "__main__":
    game = Hackamon
    game.main(Hackamon)
    print("starting main loop")